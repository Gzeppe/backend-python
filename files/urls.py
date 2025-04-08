from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-site/', admin.site.urls),
    path('', views.index, name='index'),
    path('files/', views.files, name='files'),
    path('files/<int:file_id>/', views.file, name='file'),
    path('files/edit/<int:file_id>/', views.edit, name='edit'),
    path('files/delete/<int:file_id>/', views.delete, name='delete'),
    path('files/upload/', views.upload, name='upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
