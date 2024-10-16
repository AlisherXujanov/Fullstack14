from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page, name="home"),
    path("about/", about_page, name="about"),
    path("sticky-wall/", sticky_wall, name="sticky_wall"),
    path("upcoming/", upcoming_page, name="upcoming_page"),
    path("calendar/", calendar_page, name="calendar_page"),
    path("today/", today_page, name="today_page"),
    path("settings/", settings_page, name="settings_page"),
    path("sign-out/", sign_out, name="sign_out"),
    path("create-new-todo/", create_new_todo, name="create_new_todo"),
    path("update-todo/<int:pk>", update_todo, name="update_todo"),
    path("todo-details/<int:pk>", todo_details, name="todo_details"),
    path("delete-todo/<int:pk>", delete_todo, name="delete_todo"),
]
