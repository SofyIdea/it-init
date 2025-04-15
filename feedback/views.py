from django.shortcuts import render
from .forms import ReviewForm, ResponseForm, ResponseReplyForm
from .models import Feedbacks
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import FeedbackResponse
from django.contrib.auth.decorators import login_required

def add_feedback(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'message': errors}, status=400)

def reviews_view(request):
    reviews = Feedbacks.objects.all().order_by('-created_at')
    form = ReviewForm()
    return render(request, 'reviews.html', {'reviews': reviews, 'form': form})

@login_required
@require_POST
def add_response(request):
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'message': 'Необходимо авторизоваться'})
    
    form = ResponseForm(request.POST)
    if form.is_valid():
        review_id = request.POST.get('review_id')
        try:
            review = Feedbacks.objects.get(id=review_id)
        except Feedbacks.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Отзыв не найден'})
        
        response = form.save(commit=False)
        response.author = request.user
        response.review = review
        response.save()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Ошибка в форме', 'errors': form.errors})
    
@login_required
@require_POST
def add_response_reply(request):
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'message': 'Необходимо авторизоваться'})
    
    form = ResponseReplyForm(request.POST)
    if form.is_valid():
        response_id = request.POST.get('response_id')
        try:
            parent_response = FeedbackResponse.objects.get(id=response_id)
        except FeedbackResponse.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Ответ не найден'})
        
        reply = form.save(commit=False)
        reply.author = request.user
        reply.parent_response = parent_response
        reply.save()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Ошибка в форме', 'errors': form.errors})