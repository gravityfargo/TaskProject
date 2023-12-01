from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, TagCreate
from .apiviews import TaskListApiView, TagListApiView

urlpatterns = [
    # name='' is used for routing buttons and shit
    # <a href="{% url 'task-detail' %}">

    # same class for two different urls - see the get() method
    path('', TaskList.as_view(), name="task"),
    path('<int:pk>/', TaskList.as_view(), name='task-with-detail'),
    path('by-tag/<int:tagpk>/', TaskList.as_view(), name='tasklist-by-tag'),
    path('by-tag/<int:tagpk>/<int:pk>/', TaskList.as_view(), name='tasklist-by-tag-with-detail'),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path("tag-create/", TagCreate.as_view(), name="tag-create"),

    # urls for api calls
    path('api/tasklist/', TaskListApiView.as_view(), name="api-tasks-tasklist"),
    path("api/taglist/", TagListApiView.as_view(), name="api-tasks-taglist")
    # path("api/taskcreate/", TagListApiView.as_view(), name="taskapi-create"),
    # path('api/task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    # path('api/task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    # path('api/task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
