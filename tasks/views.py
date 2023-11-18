from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task, Tag
from .forms import TagForm


# class based views, create a new object that inherets django provided classes
# specificlly for present model data

class TaskList(LoginRequiredMixin, ListView):
    model = Task

    # contextobjectname is the object you can pull data from in the template
    # {% for task in tasks %}
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'
    
    def get(self, request, *args, **kwargs):
        # checks to see if a task primary key was included in the url
        self.taskDetailID = kwargs.get('pk')
        return super(TaskList, self).get(request, *args, **kwargs)

    # Used by ListViews - it determines the list of objects that you want to display
    def get_queryset(self):
        qs = super().get_queryset()

        # ** each key-value pair of the dict is passed as a keyword argument
        self.queryfilters = { 'user': self.request.user }
        return qs.filter(**self.queryfilters)

    def get_context_data(self, **kwargs):
        # used to populate a dictionary to use as the template context. ListViews will populate the result from get_queryset's return
        context = super().get_context_data(**kwargs)
        context['incomplete'] = context['tasks'].filter(complete=False).count()
        context['tags'] = Tag.objects.filter(user=self.request.user)
        daystoday = 0
        daysnextseven = 0
        tagcounts = {}
        for task in context['tasks']:
            if task.days_away_from_due() == 0:
                daystoday += 1
            if task.days_away_from_due() <= 7:
                daysnextseven += 1

        for tag in context['tags']:
            tagcounts[tag] = context['tasks'].filter(tag__title=tag).count()
        context['tag_counts_dict'] = tagcounts
        context['due_today'] = daystoday
        context['due_next_seven_days'] = daysnextseven
        if self.taskDetailID != None:
            pk = self.taskDetailID-  1
            context['task_for_detail_view'] = context['tasks'][pk]
        else:
            context['task_for_detail_view'] = "None"


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
    
    def get_form(self, form_class=None):
        form = super(TaskCreate, self).get_form(form_class)
        form.fields["due"].widget = DatePickerInput()
        return form
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

class TagCreate(LoginRequiredMixin, FormView):
    template_name = "tasks/tag_form.html"
    form_class = TagForm
    success_url = reverse_lazy('task')

    # sets the logged in user as the 'user' for the tag 
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(TagCreate, self).form_valid(form)