from django.db import models

from accounts.models import User
from rooms.models import Room


class Booking(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    customer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bookings')

    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='bookings')

    check_in = models.DateField()

    check_out = models.DateField()

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='active')

    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer} - {self.room} ({self.check_in} to {self.check_out})"