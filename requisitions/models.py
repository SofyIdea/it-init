from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from users.models import User
from services.models import Services

class Requests(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('card', 'Карта'),
        ('offe', 'Счёт-оферта'),
        ('trea', 'Договор'),
    ]

    STATUS_CHOICES = [
        ('in_progress', 'В работе'),
        ('completed', 'Выполнено'),
        ('cancelled', 'Отменено'),
    ]

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='request_author',
        verbose_name='Автор'
    )
    email = models.EmailField(
        validators=[EmailValidator(message="Введите корректный email.")],
        verbose_name='Email'
    )
    phone = models.CharField(
        max_length=17,
        validators=[
            RegexValidator(
                regex=r'^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$',
                message="Телефон должен быть в формате +7(XXX)-XXX-XX-XX."
            )
        ],
        verbose_name='Телефон'
    )
    service = models.ForeignKey(
        Services,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Выбор услуги'
    )
    other_service_description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание другой услуги'
    )
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD_CHOICES,
        verbose_name='Способ оплаты'
    )
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default='in_progress',
        verbose_name='Статус заявки'
    )
    cancellation_reason = models.TextField(
    blank=True,
    null=True,
    verbose_name='Причина отмены'
)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Заявка от {self.author} ({self.date})"