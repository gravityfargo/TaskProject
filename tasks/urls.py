from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, TagCreate

urlpatterns = [
    # name='' is used for routing buttons and shit
    # <a href="{% url 'task-detail' %}">

    # urls for templates
    # same class for two different urls - see the get() method
    path('', TaskList.as_view(), name="task"),
    path('<int:pk>/', TaskList.as_view(), name='task-with-detail'),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path("tag-create/", TagCreate.as_view(), name="tag-create"),

    # urls for api calls
    # temp copy paste as placeholders
    # path("api/task-create/", TaskCreate.as_view(), name="task-create"),
    # path('api/task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    # path('api/task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    # path('api/task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
