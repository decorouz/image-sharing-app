from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# def update_user(sender, instance, created, **kwargs):
#     profile = instance
#     user = profile.user

#     if created == False:

#         user.save()


# post_save.connect(update_user, sender=Profile)
