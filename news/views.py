from django.shortcuts import render
from .models import Article
from services.models import Services
from users.forms import RegistrationForm, LoginForm
from feedback.models import Feedbacks, FeedbackResponse
from requisitions.forms import RequestForm
from feedback.forms import ReviewForm, ResponseForm, ResponseReplyForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ArticleForm
from django.contrib.auth.decorators import user_passes_test
from users.models import User
from django.views.decorators.http import require_POST

def list(request):
    articles = Article.objects.order_by('-date')
    services = Services.objects.all()
    feedbacks = Feedbacks.objects.all()
    feedback_response = FeedbackResponse.objects.all()
    
    form = RegistrationForm()
    form_login = LoginForm()
    form_feedback = ReviewForm()
    request_form = RequestForm()
    form_article = ArticleForm()
    response_form = ResponseForm()
    response_reply_form = ResponseReplyForm()

    return render(request, 'index.html', {
        'articles': articles, 'services': services, 'feedbacks': feedbacks, 
        'form': form, 'form_login': form_login, 'form_feedback': form_feedback,
        'request_form': request_form, 'form_article': form_article,
        'response_form': response_form, 'feedback_response': feedback_response,
        'response_reply_form': response_reply_form
        })

def paper(request, id):
    paper = Article.objects.get(id=id)
    return render(request, "paper.html", {"paper": paper})

@user_passes_test(lambda u: u.is_superuser)
@require_POST
def add_article(request):
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({
            "success": False,
            "message": "Ошибка валидации",
            "errors": form.errors
        })