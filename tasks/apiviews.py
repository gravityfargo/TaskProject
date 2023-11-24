from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer


class TaskListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            "user": request.user.id,
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "tag": request.data.get("tag"),
            "complete": request.data.get("complete"),
            "created": request.data.get("created"),
            "due": request.data.get("due"),
            "modified": request.data.get("modified"),
        }
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TagListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # list all
    def get(self, request, *args, **kwargs):
        tags = Tag.objects.filter(user=request.user)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # create
    def post(self, request, *args, **kwargs):
        data = {
            "user": request.user.id,
            "title": request.data.get("title"),
            "color": request.data.get("description"),
            "created": request.data.get("tag"),
            "modified": request.data.get("complete")
        }
        serializer = TagSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
