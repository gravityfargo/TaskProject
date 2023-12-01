from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from tasks.models import Tag

# define signals so our Profile model will be automatically created/updated when we create/update User instances. 
# Basically we are hooking the create_user_profile and save_user_profile methods to the User model, 
# whenever a save event occurs. This kind of signal is called post_save.
#CREATE USER PROFILE AND A DEFAULT TAG
@receiver(post_save, sender=User) 
def create_defaults(sender, instance, created, **kwargs):
    if created:
        Tag.objects.create(user=instance, title="Unassigned", color="#ffffff")
        Profile.objects.create(user=instance)
  