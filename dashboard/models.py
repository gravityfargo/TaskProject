from django.db import models
from django.contrib.auth.models import User
from tasks.models import Tag


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    dashboard_modules = models.TextField(max_length=500, blank=True)
    task_sort_order = models.CharField(max_length=30, blank=True)
    show_api_endpoints = models.BooleanField(default=False)
    # tags will need to be limited per user in the form definitions
    tags = models.ManyToManyField(Tag, related_name="profiles")
        
    def __str__(self):
        return self.user.username
    
    class Meta: 
        db_table = 'auth_user_profiles'
        verbose_name = 'User Profile'