from .models import Tag, Task
from django.shortcuts import redirect, render
from .models import Task, Tag
from .forms import CreateNewTag, CreateNewTask
from django.utils import timezone

def index(response):
    all_tasks = Task.objects.order_by("date_created")
    all_tags = Tag.objects.order_by("date_created")
    form = CreateNewTask()

    return render(response, "tasks/index.html", {"all_tasks": all_tasks, "all_tags":all_tags, "form": form})

def createtag(response):
    if response.method == "POST":
        form = CreateNewTag(response.POST)
        if form.is_valid():
            tagtext = form.cleaned_data["tag_text"]
            datecreated = timezone.now()
            newtag = Tag(tag_text=tagtext, date_created=datecreated)
            newtag.save()
            return redirect("tasks:index")
    elif response.method == "GET":
        form = CreateNewTag()
    
    return render(response, "tasks/createtag.html", {"form": form})

def createtask(response):
    if response.method == "POST":
        form = CreateNewTask(response.POST)
        if form.is_valid():
            tasktext = form.cleaned_data["task_text"]
            tasktag = Tag.objects.get(tag_text=form.cleaned_data["task_tag"])
            datecreated = timezone.now()
            datedue = timezone.now()
            newtask = Task(task_text=tasktext, task_tag=tasktag, date_created=datecreated, date_due=datedue)
            newtask.save()
            return redirect("tasks:index")
    return redirect("tasks:index")  # Redirect to the index page after processing the form

def deletetask(response, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("tasks:index")
