from django.shortcuts import render

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
    return render(request, "sticky_wall.html")
    