from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": "Blog Home Page"
    }
    return render(request, "home.html", context)