from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import GlobalLogin, GlobalRegister
 
urlpatterns = [
    # admin panel is a built in django feature
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),
    path('tasks/', include('tasks.urls')),
    path('login/', GlobalLogin.as_view(), name="login"),
    path('register/', GlobalRegister.as_view(), name="register"),
    # next_page is the page user is sent to after logging out
    path('logout/', LogoutView.as_view(next_page='dashboard'), name="logout")

    # path("accounts/", include("django.contrib.auth.urls")),,
    # path('tasks/', include("tasks.urls")),
]