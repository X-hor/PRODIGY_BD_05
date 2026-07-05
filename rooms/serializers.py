from rest_framework import serializers

from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        
    def validate_capacity(self, value):
        if value < 1:
            raise serializers.ValidationError("Capacity must be greater than zero.")

        return value
    
    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")

        return value
    
    