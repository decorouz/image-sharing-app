from venv import create
from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver

from actions.utils import create_action


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        create_action(instance, "has created an account")
    instance.profile.save()


# def update_user(sender, instance, created, **kwargs):
#     profile = instance
#     user = profile.user

#     if created == False:

#         user.save()


# post_save.connect(update_user, sender=Profile)
