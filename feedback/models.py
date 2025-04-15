from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

# Create your models here.
class Feedbacks(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    content = models.TextField(verbose_name='Содержимое отзыва')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Оценка'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f'Отзыв от {self.author.login} ({self.rating}/5)'
    
class FeedbackResponse(models.Model):
    review = models.ForeignKey(Feedbacks, on_delete=models.CASCADE, related_name='responses', verbose_name='Отзыв')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор ответа')
    text = models.TextField(verbose_name='Текст ответа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Ответ на отзыв'
        verbose_name_plural = 'Ответы на отзывы'
        ordering = ['created_at']

    def __str__(self):
        return f'Ответ от {self.author.login} на отзыв #{self.review.id}'

class FeedbackResponseReply(models.Model):
    parent_response = models.ForeignKey(FeedbackResponse, on_delete=models.CASCADE, 
    related_name='replies', verbose_name='Родительский ответ')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, 
    verbose_name='Автор')
    text = models.TextField(verbose_name='Текст ответа')
    created_at = models.DateTimeField(auto_now_add=True, 
    verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Ответ на комментарий'
        verbose_name_plural = 'Ответы на комментарии'
        ordering = ['created_at']

    def __str__(self):
        return f'Ответ от {self.author.login} на комментарий #{self.parent_response.id}'