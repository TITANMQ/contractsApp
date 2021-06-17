from enum import Enum

from django.db import models
from django.utils import timezone 
from django.utils.translation import ugettext_lazy as _


# user model for storing user data
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, default='default_user', unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email_address = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
    rating = models.IntegerField(default=0)



# enum for car type choices
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

# enum for status type choices
class StatusChoice(Enum):
    ON_GOING = "Ongoing"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"

# vehicle model for storing vehicle information
class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    type = models.CharField(
        max_length=10,
        choices=[(tag, tag.value) for tag in CarChoice]
    )
    capacity = models.IntegerField(default=0)
    license_plate_number = models.CharField(max_length=11, unique=True)

# customer model sub class of user
class Customer(User):
    pass

# driver model sub class of user
class Driver(User):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

# location model for storing location data 
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    latitude = models.DecimalField(decimal_places=15, max_digits=15)
    longitude = models.DecimalField(decimal_places=15, max_digits=15)

# booking model for storing booking details
class Bookings(models.Model):
    booking_id = models.AutoField(primary_key=True)
    pick_up = models.CharField(max_length=100,default="pick_up")
    drop_off = models.CharField(max_length=100, default="drop_off")
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    assigned_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    fee = models.DecimalField(decimal_places=2, max_digits=6, default=0.75)
    notes = models.CharField(max_length=100)
    status = models.CharField(max_length=30)
