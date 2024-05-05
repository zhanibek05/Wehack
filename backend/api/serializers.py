from rest_framework import serializers
from .models import parking_center, parking_place, parking_places, street_parking

class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = parking_center
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = parking_place
        fields = ['id', 'street_parking', 'num', 'active']

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = parking_places
        fields = '__all__'

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = street_parking
        fields = '__all__'
