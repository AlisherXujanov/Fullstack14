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
    