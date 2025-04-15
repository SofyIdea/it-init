from django import forms
from .models import Feedbacks, FeedbackResponse, FeedbackResponseReply

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Введите текст отзыва'}),
            'rating': forms.HiddenInput(),
        }
    
class ResponseForm(forms.ModelForm):
    class Meta:
        model = FeedbackResponse
        fields = ['text'] 
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Введите ваш ответ...'}),
        }
        
class ResponseReplyForm(forms.ModelForm):
    class Meta:
        model = FeedbackResponseReply
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 2, 
                'placeholder': 'Введите ваш ответ...',
                'class': 'response-reply-textarea'
            }),
        }