# todo/todo_api/serializers.py
from rest_framework.serializers import ModelSerializer
from .models import Task, Tag

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ["user", "title", "description", "tag", "complete", "created", "due", "modified"]

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["user", "title", "color", "created", "modified"]