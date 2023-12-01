from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, UpdateView
from .models import Profile
from .forms import ProfileForm

class GlobalLogin(LoginView):
    template_name = 'login.html'
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('dashboard')

class GlobalRegister(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(GlobalRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super(GlobalRegister, self).get(*args, **kwargs)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ProfileUpdate(LoginRequiredMixin, UpdateView):
    template_name = "dashboard/profile_form.html"
    form_class = ProfileForm
    model = Profile
    success_url = reverse_lazy("dashboard")
    
    def get_object(self, queryset=None):
        user = User.objects.get(username=self.request.user)
        return user
    
    def get_object(self):
        
        return Profile.objects.get(user=self.request.user.pk)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(ProfileUpdate, self).form_valid(form)