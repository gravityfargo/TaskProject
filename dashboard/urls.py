from django.urls import path
from .views import GlobalLogin, GlobalRegister, DashboardView, ProfileUpdate

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', GlobalLogin.as_view(), name="login"),
    path('register/', GlobalRegister.as_view(), name="register"),
    path('profile/<user>/', ProfileUpdate.as_view(), name="profile"),
]