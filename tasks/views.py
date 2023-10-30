from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# class based views, create a new object that inherets django provided classes
# specificlly for present model data

class TaskList(ListView):
    model = Task
    # contextobjectname is the object you can pull data from in the template
    # {% for task in tasks %}
    context_object_name = 'tasks'
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task.html'

class TaskCreate(CreateView):
    # createview shows a form
    model = Task
    # can use a list ['field1', ...]
    fields = '__all__'
    # template name from urls
    success_url = reverse_lazy('task')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task')