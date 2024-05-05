from django.urls import path
from api.views import *
from api import views

urlpatterns = [
    path('users/', views.user),
    path('parkings/', views.parkingList, name = "parkingsList"),
    path('parkings/<int:id>/', views.parkingListDetail, name = "parkingsListDetail"),
    path('parkings/<int:id>/num/', views.parking_num),
    path('parkingplace/<int:id>/', views.parkingPlaceDetail, name = "parkingsPlaceDetail"),
    path('parkings/update/<int:id>/', views.UpdateParkingInfo, name = "parkingsUpdate"),
    path('parkingstreet/update/<int:id>/', views.UpdateStreetParkingInfo, name = "streetUpdate"),
    path('parking/street/', views.streetIntersection, name = "parkingsUpdate"),
]