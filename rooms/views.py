from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import datetime

from bookings.models import Booking
from .filters import RoomFilter
from .models import Room
from .serializers import RoomSerializer



class RoomViewSet(viewsets.ModelViewSet):

    queryset = Room.objects.all()

    serializer_class = RoomSerializer
    
    filter_backends = [DjangoFilterBackend]

    filterset_class = RoomFilter
    
    def get_permissions(self):

        if self.action in ["create", "update", "partial_update", "destroy",]:
            return [IsAdmin()]

        return [IsAuthenticated()]
    
    
    @action(detail=False,methods=["get"])
    def available(self, request):
        today = timezone.localdate()
        check_in = request.query_params.get("check_in")
        check_out = request.query_params.get("check_out")
        
        if not check_in or not check_out:
            return Response(
                {"error": "check_in and check_out are required"}, 
                status=400
                )
            
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()

        check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()
        
        if check_in_date < today:
            return Response(
                {"error": "Check-in date cannot be in the past."},
                status=400
            )
            
        if check_out_date <= check_in_date:
            return Response(
                {"error": "Check-out date must be after check-in."},
                status=400
            )
            
        booked_rooms = Booking.objects.filter(
            status="active",
            check_in__lt=check_out,
            check_out__gt=check_in,
        ).values_list("room_id",flat=True)
        
        available_rooms = Room.objects.filter(is_active=True).exclude(id__in=booked_rooms)
                
        serializer = RoomSerializer(available_rooms, many=True)

        return Response(serializer.data)