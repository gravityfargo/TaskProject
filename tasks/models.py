import imp
from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    # cascade if user deleted, will deleted its tasks
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length = 200, null=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
    # Model metadata is “anything that’s not a field”, 
    # such as ordering options (ordering), 
    # database table name (db_table), 
    # or human-readable singular and plural names
    class Meta:
        ordering = ['complete']