from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("createtag/", views.createtag, name="createtag"),
    path("createtask/", views.createtask, name="createtask"),
    path("deletetask/<int:id>", views.deletetask, name="deletetask"),
]