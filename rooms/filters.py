import django_filters

from .models import Room


class RoomFilter(django_filters.FilterSet):

    max_price = django_filters.NumberFilter(field_name="price_per_night",lookup_expr="lte")

    min_price = django_filters.NumberFilter(field_name="price_per_night",lookup_expr="gte")

    class Meta:
        model = Room

        fields = ["room_type", "capacity", "is_active",]