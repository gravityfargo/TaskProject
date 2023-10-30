from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin panel is a built in django feature
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),

    # path("accounts/", include("django.contrib.auth.urls")),
    # path("register/", taskviews.register, name="register"),
    # path('tasks/', include("tasks.urls")),
    # path('', include("django.contrib.auth.urls")),
]