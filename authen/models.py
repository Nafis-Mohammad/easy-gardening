# models.py
from django.db import models
from django.contrib.auth.models import User
import datetime
# Creating the Userprofile model


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # Revert back to 'avatar' field name
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username



