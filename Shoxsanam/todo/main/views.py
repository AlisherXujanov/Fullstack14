from django.shortcuts import render, redirect, get_object_or_404
from .models import Todos 
from .forms import TodosForm 
from django.contrib import messages


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
    

def create_new_todo(request):
    if request.method == "POST":
        form = TodosForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.owner = request.user
            form.save()
            messages.success(request, "Todo created successfully")
            return redirect("sticky_wall")

    form = TodosForm()
    context = {
        "title": "Create New Todo",
        "form": form,
    }
    return render(request, "create-new-todo.html", context)


def update_todo(request, pk:int):
    todo_item = get_object_or_404(Todos, id=pk)

    if request.method == "POST":
        form = TodosForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo updated successfully")
            return redirect("sticky_wall")

    form = TodosForm(instance=todo_item)
    context = {
        "title": "Update Todo",
        "form": form,
    }
    return render(request, "update-todo.html", context)


def delete_todo(request, pk:int):
    todo_item = get_object_or_404(Todos, id=pk)
    todo_item.delete()
    messages.warning(request, "Todo deleted")
    return redirect("sticky_wall")


def todo_details(request, pk:int):
    todo = get_object_or_404(Todos, id=pk)
    context = {
        "todo": todo,
        "title": todo.title + " details",
    }
    return render(request, "todo_details.html", context)
    
