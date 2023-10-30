from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    # name='' is used for routing buttons and shit
    # <a href="{% url 'task-detail' %}">

    # by default loads the task_list.html template
    path('', TaskList.as_view(), name='task'),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete')
]
