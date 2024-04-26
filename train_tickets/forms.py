from django import forms
from train_tickets.models import Booking, Place

class PlaceAdd(forms.ModelForm):
    class Meta:
        model = Place
        fields = ["place", "description", "short_description", "image"]

class TicketAdd(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["user", "place", "date", "time"]
        widgets = {
            "media": forms.FileInput()
        }


