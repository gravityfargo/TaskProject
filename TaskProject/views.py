from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class GlobalLogin(LoginView):
    template_name = 'login.html'
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('dashboard')