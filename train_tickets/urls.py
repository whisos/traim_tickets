from django.urls import path
from train_tickets.views import *

urlpatterns = [
    path('', index, name = "index"),
]
