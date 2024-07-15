from rest_framework import serializers
from .models import Dish


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['name', 'location', 'items', 'lat_long', 'full_details']
        depth = 1