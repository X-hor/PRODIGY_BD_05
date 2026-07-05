from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("receptionist", "Receptionist"),
        ("customer", "Customer"),
    ]

    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='customer')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username