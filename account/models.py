from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


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


class Contact(models.Model):
    user_from = models.ForeignKey(
        "auth.User", related_name="rel_from_set", on_delete=models.CASCADE)
    user_to = models.ForeignKey(
        "auth.User", related_name="rel_to_set", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self) -> str:
        return f"{self.user_from} follows {self.user_from}"

# user_from:  A ForeignKey for the use who creates the relationship
# user_to : A foreignKey for the user being followed


# Add following filed to User dynamically
user_model = get_user_model()  # return the currently active User model
user_model.add_to_class("following",
                        models.ManyToManyField("self", through=Contact, related_name="followers", symmetrical=False))
