from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from requisitions.models import Requests
from requisitions.forms import RequestForm
from services.models import Services

@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return JsonResponse({'success': True, 'message': 'Регистрация прошла успешно!'})
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    return JsonResponse({'success': False, 'message': 'Неверный метод запроса.'})
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Неверное имя пользователя или пароль.'}, status=400)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'message': errors}, status=400)

@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': True, 'message': 'Вы успешно вышли.'})
    
def user_profile(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')  
    
    user_requests = Requests.objects.filter(author=user).order_by('-date')
    services = Services.objects.all()
    request_form = RequestForm()
    
    context = {
        'user': user,
        'requests': user_requests,
        'request_form': request_form,
        'services': services
    }
    return render(request, 'profile.html', context)