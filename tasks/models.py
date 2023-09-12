import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Tag(models.Model):
    # attributes
    tag_text = models.CharField(max_length=10, unique=True, blank=True)
    date_created = models.DateField()
    # method to return a human readable represention of the object
    def __str__(self):
        return self.tag_text
    
    # custom method to return the time delta since creation
    def days_since_creation(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=1)

    # custom method to return the time delta with regards to the due date
    def days_away_from_due(self):
        return self.date_due >= timezone.now() - datetime.timedelta(days=1)


class Task(models.Model):
    task_text = models.CharField(max_length=50)
    task_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    date_created = models.DateField()
    date_due = models.DateField()

    def __str__(self):
        return self.task_text