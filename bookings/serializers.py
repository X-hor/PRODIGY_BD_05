from rest_framework import serializers
from django.utils import timezone

from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ["customer","status",]
  
    def validate(self, attrs):
        today = timezone.localdate()

        if attrs["check_in"] < today:
            raise serializers.ValidationError(
                "Check-in date cannot be in the past."
            )
            
        if (attrs["check_out"]<= attrs["check_in"]):
            raise serializers.ValidationError("Check-out must be after check-in.")
        return attrs
    
        room = attrs["room"]
        if not room.is_active :
            raise serializers.ValidationError("Room is unavailable!")
        
        overlapping = Booking.objects.filter(
            room=room,
            status="active",
            check_in__lt=attrs["check_out"],
            check_out__gt=attrs["check_in"],
        ).exists()
        if overlapping :
            raise serializers.ValidationError("Room is already booked for these dates!")