from django.views.generic import ListView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task, Tag
from .forms import TagForm, TaskForm


# class based views, create a new object that inherets django provided classes
# specificlly for present model data


class TaskList(LoginRequiredMixin, ListView):
    model = Task

    # contextobjectname is the object you can pull data from in the template
    # {% for task in tasks %}
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"

    def get(self, request, *args, **kwargs):
        # checks to see if a task primary key was included in the url
        self.taskDetailID = kwargs.get("pk")
        self.tagFilter = kwargs.get("tagpk")
        return super(TaskList, self).get(request, *args, **kwargs)

    # Used by ListViews - it determines the list of objects that you want to display
    # the objects are provided from the return of get()
    def get_queryset(self):
        qs = super().get_queryset()

        # each key-value pair of the dict is passed as a keyword argument
        # used to filter all results before get_context_data
        if self.tagFilter is not None:
            self.queryfilters = {"user": self.request.user, "tag": self.tagFilter}
        else:
            self.queryfilters = {"user": self.request.user}
            
        return qs.filter(**self.queryfilters)

    def get_context_data(self, **kwargs):
        # used to populate a dictionary to use as the template context. ListViews will populate the result from get_queryset's return
        context = super().get_context_data(**kwargs)

        context["incomplete"] = context["tasks"].filter(complete=False).count()
        context["tags"] = Tag.objects.filter(user=self.request.user)
        for tag in context["tags"]:
            # execute the method for each tag to get its updated count
            tag.count(self.request.user)

        daystoday = 0
        daysnextseven = 0
        for task in context["tasks"]:
            if task.days_away_from_due() is not None:
                if task.days_away_from_due() == 0:
                    daystoday += 1
                if task.days_away_from_due() <= 7:
                    daysnextseven += 1
        context["due_today"] = daystoday
        context["due_next_seven_days"] = daysnextseven

        if self.taskDetailID != None:
            pk = self.taskDetailID
            for task in context["tasks"]:
                if task.pk == pk:
                    context["task_for_detail_view"] = task
        else:
            context["task_for_detail_view"] = "None"

        return context


class TaskCreate(LoginRequiredMixin, FormView):
    template_name = "tasks/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task")
    
    # pass the current user to the ModelForm instance using a kwarg
    def get_form_kwargs(self):
        kwargs = super(TaskCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    template_name = "tasks/task_form.html"
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy("task")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(TaskUpdate, self).form_valid(form)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("task")


class TagCreate(LoginRequiredMixin, FormView):
    template_name = "tasks/tag_form.html"
    form_class = TagForm
    success_url = reverse_lazy("task")

    # sets the logged in user as the 'user' for the tag
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(TagCreate, self).form_valid(form)
