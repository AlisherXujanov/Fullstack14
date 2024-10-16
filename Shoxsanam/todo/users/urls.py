from django.urls import path
from .views import *

urlpatterns = [
    path("profile-settings", profile_settings, name="profile_settings"),
]
