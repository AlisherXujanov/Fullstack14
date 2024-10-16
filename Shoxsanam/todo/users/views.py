from django.shortcuts import render
from .models import Profile

# Create your views here.
def profile_settings(request):
    profile_obj = Profile.objects.get(user=request.user)

    context = {
        "title": "Profile Settings of: " + request.user.username,
        "profile_obj": profile_obj
    }
    return render(request, 'profile_settings.html', context)
