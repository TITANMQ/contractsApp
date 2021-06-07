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

class Customer(models.Model, User):
    pass

class Driver(models.Model, User):
    vehicle = models.CharField(Vehicle)

class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    latitude = models.DecimalField(max_digits=15)
    longitude = models.DecimalField(max_digits=15)

class CarChoice(Enum):
    TUK = "TUK-TUK"
    MINI = "MINI-VAN"
    SUV = "SPORT-UTILITY VEHICLE"
    CONV = "CONVERTIBLE"
    COUP = "COUPE"
    # LUX cars are for future features.
    LUX_SUV = "LUXURY SPORT-UTILITY VEHICLE"
    LUX_CONV = "LUXURY CONVERTIBLE"
    LUX_COUP = "LUXURY COUPE"

class Vehicle(models.Model):
    vehicle_id = models.IntegerField(primary_key=True)
    type = models.CharField(
        max_length=10,
        choices=[(tag, tag.value) for tag in CarChoice]
    )
    capacity = models.IntegerField(default=0)
    license_plate_number = models.CharField(max_length=11)