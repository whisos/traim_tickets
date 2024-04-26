from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    place = models.CharField(max_length=30)
    short_description = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    image = models.FileField(upload_to="place_media/",null=True, blank=True)

    def __str__(self):
        return f"{self.place}"

class Booking(models.Model):
    time = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add =True)
