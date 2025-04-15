from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve as mediaserve
from django.urls import re_path as url  # Исправленный импорт

urlpatterns = [
    path("admin/", admin.site.urls),
    path('admin-panel/', include('admin_panel.urls')),
    path('', include('news.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# else: 
#     urlpatterns += [
#         url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), 
#             mediaserve, {'document_root': settings.MEDIA_ROOT}),
#         url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.strip('/'), 
#             mediaserve, {'document_root': settings.STATIC_ROOT}),
#     ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]