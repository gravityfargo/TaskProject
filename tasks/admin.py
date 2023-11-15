from django.contrib import admin
from .models import Task, Tag

# Register models to be visible in the admin panel
admin.site.register(Task)
admin.site.register(Tag)