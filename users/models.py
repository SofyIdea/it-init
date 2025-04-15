from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class UserManager(BaseUserManager):
    def create_user(self, login, password, full_name, phone, email):
        if not login:
            raise ValueError("Логин обязателен.")
        if not password:
            raise ValueError("Пароль обязателен.")
        if not full_name:
            raise ValueError("ФИО обязательно.")
        if not phone:
            raise ValueError("Телефон обязателен.")
        if not email:
            raise ValueError("Email обязателен.")

        user = self.model(
            login=login,
            full_name=full_name,
            phone=phone,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password, full_name, phone, email):
        user = self.create_user(
            login=login,
            password=password,
            full_name=full_name,
            phone=phone,
            email=email,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9]+$',
                message="Логин должен содержать только латиницу и цифры."
            )
        ],
        verbose_name='Логин'
    )

    password = models.CharField(max_length=128, verbose_name='Пароль')

    full_name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[а-яА-ЯёЁ\s]+$',
                message="ФИО должно содержать только кириллицу и пробелы."
            )
        ],
        verbose_name='ФИО'
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

    email = models.EmailField(
        unique=True,
        validators=[EmailValidator(message="Введите корректный email.")],
        verbose_name='Email'
    )

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')

    objects = UserManager()

    USERNAME_FIELD = 'login'  
    REQUIRED_FIELDS = ['full_name', 'phone', 'email']  

    def __str__(self):
        return self.login