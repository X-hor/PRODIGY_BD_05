from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "delete"]
    
    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return Booking.objects.all()

        return Booking.objects.filter(
            customer=user
        )
        
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)