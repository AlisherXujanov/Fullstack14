from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": "Blog Home Page"
    }
    return render(request, "home.html", context)

def blog(request):
    return render(request, "blog.html")

def news(request):
    return render(request, "news.html")

def about(request):
    return render(request, "about.html")

def create(request):
    return render(request, "create.html")