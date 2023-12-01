from django.contrib import admin
from .models import Task, Tag

# Register models to be visible in the admin panel
class AdminTask(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'tag']

class AdminTag(admin.ModelAdmin):
    list_display = ['user', 'title', 'color']

admin.site.register(Task, AdminTask)
admin.site.register(Tag, AdminTag)