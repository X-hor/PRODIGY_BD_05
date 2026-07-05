from django.db import models

from accounts.models import User


class Room(models.Model):

    ROOM_TYPES = [
        ("single", "Single"),
        ("double", "Double"),
        ("suite", "Suite"),
    ]

    room_number = models.PositiveIntegerField(unique=True)

    floor_number = models.PositiveIntegerField(default=0)

    room_type = models.CharField(max_length=20,choices=ROOM_TYPES)

    capacity = models.PositiveIntegerField()

    price_per_night = models.DecimalField(max_digits=10,decimal_places=2)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Room {self.room_number}"