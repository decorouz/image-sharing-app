from tkinter import CASCADE
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Profile for user {self.user.username}"
# Create your models here.
