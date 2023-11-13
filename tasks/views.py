from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task

# class based views, create a new object that inherets django provided classes
# specificlly for present model data

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    # contextobjectname is the object you can pull data from in the template
    # {% for task in tasks %}
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # when the page is loaded, this class will take the 'task' model object (task table in the database)
        # this filter only allow tasks for the logged in user who sent the request (loaded the page)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    # createview shows a form
    model = Task
    # which fields are shown to the user
    fields = ['title', 'description', 'tag', 'due']
    # template name from urls
    success_url = reverse_lazy('task')

    # sets the logged in user as the 'user' for the task 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'tag', 'due']
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task')