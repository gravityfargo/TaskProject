from django.shortcuts import render
from .models import Task, Tag
from .forms import CreateNewTag
from django.utils import timezone

all_tasks = Task.objects.order_by("date_created")
context = {
"all_tasks": all_tasks
}

def index(response):
    return render(response, "tasks/index.html", {"all_tasks": all_tasks})

def createtag(response):
    if response.method == "POST":
        form = CreateNewTag(response.POST)
        if form.is_valid():
            tagtext = form.cleaned_data["tag_text"]
            datecreated = timezone.now()
            newtag = Tag(tag_text=tagtext, date_created=datecreated)
            newtag.save()
    else:
        form = CreateNewTag(response.POST)
    return render(response, "tasks/createtag.html", {"form": form})
