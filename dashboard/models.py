from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dashboard_modules = models.TextField(max_length=500, blank=True)
    task_sort_order = models.CharField(max_length=30, blank=True)
    show_api_endpoints = models.BooleanField(default=False)
    
    # define signals so our Profile model will be automatically created/updated when we create/update User instances. 
    # Basically we are hooking the create_user_profile and save_user_profile methods to the User model, 
    # whenever a save event occurs. This kind of signal is called post_save.
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    def __str__(self):
        return self.user.username