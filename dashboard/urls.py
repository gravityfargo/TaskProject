from django.urls import path
from .views import GlobalLogin, GlobalRegister, DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', GlobalLogin.as_view(), name="login"),
    path('register/', GlobalRegister.as_view(), name="register"),
]