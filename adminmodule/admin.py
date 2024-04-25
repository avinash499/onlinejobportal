from django.contrib import admin

# Register your models here.
# models.py

from django.db import models
from django.contrib.auth.models import User


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"Password reset for {self.user.username}"
