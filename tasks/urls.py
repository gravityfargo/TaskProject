from django.urls import include, path
from rest_framework import routers
from . import views
from .apiviews import TaskListApiView, TaskDetailApiView, UserViewSet, GroupViewSet

app_name = "tasks"
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("createtag/", views.createtag, name="createtag"),
    path("createtask/", views.createtask, name="createtask"),
    path("deletetask/<int:id>", views.deletetask, name="deletetask"),
    
    # API to retrieve 
    path('api/', include(router.urls)),
    path('api/tasklist/', TaskListApiView.as_view()),
    path('api/<int:tid>/', TaskDetailApiView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]