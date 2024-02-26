from django.shortcuts import render
from train_tickets.models import *


def index(request):
    places = Place.objects.all()
    content = {"places":places}
    return render(request, "train_tickets/index.html", content)


def place_detail(request, place_id):
    place = Place.objects.get(id=place_id)
    content = {"place":place}
    return render(request, "train_tickets/detail.html", content)
