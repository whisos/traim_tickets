from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length= 30)
    surname = models.CharField(max_length=30)

class Place(models.Model):
    place = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField()

class Booking(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add =True)