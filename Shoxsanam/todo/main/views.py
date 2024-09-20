from django.shortcuts import render
from .models import Todos 

# Create your views here.
def home_page(request):
    context = {
        "title": "Welcome to Django App",
    }
    return render(request, "home.html", context)


def about_page(request):
    context = {
        "title": "About Us",
    }
    return render(request, "about.html", context)


def sticky_wall(request):
    context = {
        'todos': Todos.objects.all()
    }
    return render(request, "sticky_wall.html", context)


def upcoming_page(request):
    context = {
        "title": "Upcoming",
    }
    return render(request, "upcoming.html",context)


def calendar_page(request):
    context = {
        "title": "Calendar",
    }
    return render(request, "calendar.html",context)


def today_page(request):
    context = {
        "title": "Today",
    }
    return render(request, "today.html",context)


def settings_page(request):
    context = {
        "title": "Settings",
    }
    return render(request, "settings.html",context)


def sign_out(request):
    context = {
        "title": "Sign Out",
    }
    return render(request, "sign-out.html",context)
    
