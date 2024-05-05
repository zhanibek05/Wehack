from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse, Http404
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Users
from .models import parking_center, parking_place, parking_places, street_parking
from .serializers import CenterSerializer, PlaceSerializer, PlacesSerializer, StreetSerializer

@api_view(['GET', 'POST', 'DELETE'])
def user(request):
    if request.method == 'GET':
        accounts = Users.objects.all()
        accounts_json = [account.to_json() for account in accounts]
        return JsonResponse(accounts_json, safe=False)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')  
        account = Users.objects.create(
            id=id,
            nickname=data.get('name', ''),
            mail=data.get('mail', ''),
            password = data.get('password', '')
        )
        return JsonResponse(account.to_json())

    if request.method == 'DELETE':
        data = json.loads(request.body)
        id = data.get('id')
        try:
            user = Users.objects.get(pk=id)
            user.delete()
            return Response('User successfully deleted!')
        except Users.DoesNotExist:
            return Response('User does not exist!', status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def parkingList(request):
    parkings = parking_center.objects.all()
    serializer = CenterSerializer(parkings, many = True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def parkingListDetail(request, id):
    parkings = parking_center.objects.get(pk = id)
    serializer = CenterSerializer(parkings, many = False)
    return JsonResponse(serializer.data,safe=False)


@api_view(['GET', 'POST'])
def parking_num(request, id):
    if request.method == 'GET':
        vacancies = parking_places.objects.filter(parking_center_id=id)
        serializer = PlacesSerializer(vacancies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        data['parking_center_id'] = id
        serializer = PlacesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def parkingPlaceDetail(request, id):
    parkings = parking_place.objects.get(pk = id)
    serializer = CenterSerializer(parkings, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def streetIntersection(request):
    intersections = street_parking.objects.all()
    serializer = StreetSerializer(intersections, many = True)
    return Response(serializer.data)

@api_view(['PUT'])
def UpdateParkingInfo(request, id):
    parking = parking_places.objects.get(pk = id)
    serializer = PlacesSerializer(instance = parking, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def UpdateStreetParkingInfo(request, id):
    parking = parking_place.objects.get(pk = id)
    serializer = PlaceSerializer(instance = parking, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

