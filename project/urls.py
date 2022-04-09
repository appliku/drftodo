from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('accounts/', include('allauth.urls')),
    path(settings.ADMIN_URL, admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
