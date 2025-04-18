# Generated by Django 5.1.2 on 2025-03-30 18:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "login",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Логин должен содержать только латиницу и цифры.",
                                regex="^[a-zA-Z0-9]+$",
                            )
                        ],
                        verbose_name="Логин",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="Пароль")),
                (
                    "full_name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="ФИО должно содержать только кириллицу и пробелы.",
                                regex="^[а-яА-ЯёЁ\\s]+$",
                            )
                        ],
                        verbose_name="ФИО",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=17,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Телефон должен быть в формате +7(XXX)-XXX-XX-XX.",
                                regex="^\\+7\\(\\d{3}\\)-\\d{3}-\\d{2}-\\d{2}$",
                            )
                        ],
                        verbose_name="Телефон",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        unique=True,
                        validators=[
                            django.core.validators.EmailValidator(
                                message="Введите корректный email."
                            )
                        ],
                        verbose_name="Email",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активен"),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="Персонал"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
