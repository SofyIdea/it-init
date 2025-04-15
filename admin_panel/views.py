from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from requisitions.models import Requests

def is_admin(user):
    return user.is_authenticated and user.is_staff

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Неверные данные или вы не являетесь администратором.'})
    
    return render(request, 'login.html')

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    requests = Requests.objects.all().select_related('author', 'service').order_by('-date')
    return render(request, 'dashboard.html', {'requests': requests})

@login_required
@user_passes_test(is_admin)
def update_request_status(request, request_id):
    if request.method == 'POST':
        status = request.POST.get('status')
        cancellation_reason = request.POST.get('cancellation_reason', '')

        req = Requests.objects.get(id=request_id)

        req.status = status

        if status == 'cancelled':
            req.cancellation_reason = cancellation_reason
        else:
            req.cancellation_reason = ''

        req.save()
        
        return redirect('admin_dashboard')

    return HttpResponse("Метод GET не поддерживается", status=405)