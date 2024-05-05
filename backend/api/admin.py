from django.contrib import admin
from .models import Users, parking_center, parking_places, street_parking, parking_place

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')

@admin.register(parking_center)
class ParkingCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(parking_places)
class ParkingPlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'parking_center', 'num', 'levels', 'active')

@admin.register(street_parking)
class StreetParkingAdmin(admin.ModelAdmin):
    list_display = ('id', 'street1', 'street2')

@admin.register(parking_place)
class ParkingPlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'street_parking', 'num', 'active')
