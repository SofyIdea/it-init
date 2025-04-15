from django.contrib import admin
from .models import Requests

class RequestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'email', 'phone', 'service', 'payment_method', 'status', 'date')
    search_fields = ('author__username', 'email', 'phone')
    list_filter = ('status', 'payment_method', 'date')
    list_editable = ('status',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('id', 'author', 'email', 'phone', 'service', 'other_service_description')
        }),
        ('Дополнительная информация', {
            'fields': ('payment_method', 'status', 'cancellation_reason', 'date')
        }),
    )
    readonly_fields = ('id', 'date')

    class Media:
        js = ('js/admin_requests.js',) 

admin.site.register(Requests, RequestsAdmin)