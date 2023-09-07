from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_text = models.CharField(max_length=10)
    date_created = models.DateField()
    date_due = models.DateField()

class Task(models.Model):
    task_text = models.CharField(max_length=50)
    task_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    date_created = models.DateField()
    date_due = models.DateField()