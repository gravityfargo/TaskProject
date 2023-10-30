import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    # cascade if user deleted, will deleted its tasks
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    tag = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    modified = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def days_since_creation(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def days_away_from_due(self):
        return self.due >= timezone.now() - datetime.timedelta(days=1)

    # Model metadata is “anything that’s not a field”,
    # such as ordering options (like i.e. sorting),
    # database table name (db_table),
    # or human-readable singular and plural names
    class Meta:
        ordering = ["complete"]

class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    modified = models.DateTimeField(auto_now_add=False, null=True, blank=True)
  
    def __str__(self):
        return self.title
