# Generated by Django 5.1.2 on 2025-03-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=150)),
                ("content", models.TextField()),
                ("date", models.DateField(auto_now_add=True)),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
    ]
