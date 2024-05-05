from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class parking_center(models.Model):
    name = models.CharField(max_length=255)

class parking_places(models.Model):
    parking_center = models.ForeignKey(parking_center, on_delete=models.CASCADE, null=True, blank=True)
    num = models.IntegerField(default=0)
    levels = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

class street_parking(models.Model):
    street1 = models.CharField(max_length=255, default='')
    street2 = models.CharField(max_length=255, default='')

class parking_place(models.Model):
    street_parking = models.ForeignKey(street_parking, on_delete=models.CASCADE, null=True, blank=True)
    num = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
