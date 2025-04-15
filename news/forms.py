from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
        labels = {
            'title': 'Заголовок',
            'content': 'Текст статьи',
            'image': 'Изображение',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),  # Увеличим высоту поля
        }