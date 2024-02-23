from django.shortcuts import render
from train_tickets.models import *


def index(request):
    return render(request, "train_tickets/index.html")
