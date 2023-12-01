from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # admin panel is a built in django feature
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('tasks/', include('tasks.urls')),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name="logout")
]