from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Receiver function"""
    if created:
        new_user = instance
        profile = Profile.objects.create(
            user=new_user

        )


def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:

        user.save()


post_save.connect(update_user, sender=Profile)
