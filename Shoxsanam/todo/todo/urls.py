"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home_page),
    path("about/", about_page, name="about"),
    path("sticky_wall/", sticky_wall, name="sticky_wall"),
    path("upcoming/", upcoming_page, name="upcoming_page"),
    path("calendar/", calendar_page, name="calendar_page"),
    path("today/", today_page, name="today_page"),
    path("settings/", settings_page, name="settings_page"),
    path("sign-out/", sign_out, name="sign-out"),
    
    # =========================================
    # ADMIN
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
