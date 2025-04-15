from django.contrib import admin
from .models import Services


# Register your models here.
@admin.register(Services)
class ServiscesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'about', 'price')