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

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs["publisher"])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # when the page is loaded, this class will take the 'task' model object (task table in the database)
        # this filter only allow tasks for the logged in user who sent the request (loaded the page)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
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


        
        # future search function
        # # gets text from the 'search' (name of html element) bar in the nav, can be empty
        # search_input = self.request.GET.get('search') or ''
        # if search_input:
        #     # filters the tasks again by the search term
        #     context['task'] = context['task'].filter(title__icontains = search_input)
        #     context['search_input'] = search_input
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