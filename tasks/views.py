from rest_framework import viewsets, permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer, TaskSerializer
from .models import Tag, Task

class TagListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        tags = Tag.objects.filter(created_by_user = request.user.id)
        serializer = TaskSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        todos = Task.objects.filter(created_by_user = request.user.id)
        serializer = TaskSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, tid, uid):
        # Helper method to get the object with given todo_id, and user_id
        try:
            return Task.objects.get(id=tid, created_by_user = uid)
        except Task.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, tid, *args, **kwargs):
        # Retrieves the Todo with given todo_id
        task_instance = self.get_object(tid, request.user.id)
        if not task_instance:
            return Response(
                {"res": "task object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TaskSerializer(task_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, tid, *args, **kwargs):
        # Updates the todo item with given todo_id if exists
        task_instance = self.get_object(tid, request.user.id)
        if not task_instance:
            return Response(
                {"res": "that task object not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task_text': request.data.get('task'), 
            'completedstatus': request.data.get('completed'), 
            'created_by_user': request.user.id
        }
        serializer = TaskSerializer(instance = task_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, todo_id, *args, **kwargs):
        # Deletes the todo item with given todo_id if exists
        task_instance = self.get_object(todo_id, request.user.id)
        if not task_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        task_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class UserViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    # API endpoint that allows groups to be viewed or edited.
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# from django.shortcuts import redirect, render
# from .models import Task, Tag
# from .forms import CreateNewTag, CreateNewTask
# from django.utils import timezone


# def index(response):
#     all_tasks = Task.objects.order_by("date_created")
#     all_tags = Tag.objects.order_by("date_created")
#     form = CreateNewTask()
#     return render(response, "tasks/index.html", {"all_tasks": all_tasks, "all_tags":all_tags, "form": form})

# def createtag(response):
#     if response.method == "POST":
#         form = CreateNewTag(response.POST)
#         if form.is_valid():
#             tagtext = form.cleaned_data["tag_text"]
#             datecreated = timezone.now()
#             newtag = Tag(tag_text=tagtext, date_created=datecreated)
#             newtag.save()
#             return redirect("tasks:index")
#     elif response.method == "GET":
#         form = CreateNewTag()
        
#     return render(response, "tasks/createtag.html", {"form": form})

# def createtask(response):
#     if response.method == "POST":
#         form = CreateNewTask(response.POST)
#         if form.is_valid():
#             tasktext = form.cleaned_data["task_text"]
#             tasktag = Tag.objects.get(tag_text=form.cleaned_data["task_tag"])
#             datecreated = timezone.now()
#             datedue = timezone.now()
#             newtask = Task(task_text=tasktext, task_tag=tasktag, date_created=datecreated, date_due=datedue)
#             newtask.save()
#             return redirect("tasks:index")
#     return redirect("tasks:index")  # Redirect to the index page after processing the form

    
# def deletetask(response, id):
#     task = Task.objects.get(id=id)
#     task.delete()
#     return redirect("tasks:index")
