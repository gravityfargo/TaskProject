from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task, Tag

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["task_text", "task_tag", "date_created", "date_due", "date_modified", "created_by_user", "completedstatus"]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["tag_text", "date_created", "date_modified", "created_by_user"]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']