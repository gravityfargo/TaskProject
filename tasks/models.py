import datetime
from django.db import models
from django.utils import timezone

def default_tag():
        return 0

class Tag(models.Model):
    tag_text = models.CharField(max_length=10, unique=True, blank=True)
    date_created = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_modified = models.DateTimeField(auto_now_add = True, blank=True)
    created_by_user =  models.CharField(max_length = 180, blank=True)
    
    def __str__(self):
        return self.tag_text


class Task(models.Model):
    task_text = models.CharField(max_length = 180, blank=True)
    task_tag = models.ForeignKey(Tag, on_delete = models.CASCADE, default=default_tag)
    date_created = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_due = models.DateTimeField(auto_now = True, null=True)
    date_modified = models.DateTimeField(auto_now = True, blank = True)
    created_by_user =  models.CharField(max_length = 180, blank=True)
    completedstatus = models.BooleanField(default = False, blank = True)
    
    def __str__(self):
        return self.task_text
       
    def days_since_creation(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=1)

    def days_away_from_due(self):
        return self.date_due >= timezone.now() - datetime.timedelta(days=1)