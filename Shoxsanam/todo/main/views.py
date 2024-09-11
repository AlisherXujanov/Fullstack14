from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {
        "title": "Welcome to Django Todo App",
    }
    return render(request, "home.html", context)


def about_page(request):
    context = {
        "title": "About Us",
    }
    return render(request, "about.html", context)