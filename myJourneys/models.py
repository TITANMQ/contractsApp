from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email_address = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
    rating = models.IntegerField()

class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    latitude = models.DecimalField(max_digits=15)
    longitude = models.DecimalField(max_digits=15)