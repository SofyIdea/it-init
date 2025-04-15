from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import RequestForm

@csrf_exempt
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            if not request.user.is_authenticated:
                return JsonResponse({'success': False, 'message': 'Пользователь не авторизован.'})
            
            request_instance = form.save(commit=False)
            request_instance.author = request.user 
            request_instance.save()
            return JsonResponse({'success': True, 'message': 'Заявка успешно отправлена!'})
        else:
            errors = {field: form.errors[field] for field in form.errors}
            return JsonResponse({'success': False, 'errors': errors})
    return JsonResponse({'success': False, 'message': 'Неверный метод запроса.'})