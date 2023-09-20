from django.urls import include, path
from rest_framework import routers
from . import views
from .views import TaskListApiView, TaskDetailApiView

app_name = "tasks"
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # path("", views.index, name="index"),
    # path("createtag/", views.createtag, name="createtag"),
    # path("createtask/", views.createtask, name="createtask"),
    # path("deletetask/<int:id>", views.deletetask, name="deletetask"),
    path('', include(router.urls)),
    path('api', TaskListApiView.as_view()),
    path('api/<int:tid>/', TaskDetailApiView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]