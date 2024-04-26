from django.urls import path
from train_tickets.views import *

urlpatterns = [
    path('', PlaceListView.as_view(), name = "place_list"),
    path('<int:pk>/', PlaceDetailView.as_view(), name = "place_detail"),
    path('place_add/', PlaceAddView.as_view(), name="place_add"),
    path('booking_add/', BookingAddView.as_view(), name="booking_add"),
    path('booking_list/', BookingListView.as_view(), name = "booking_list"),
    path('booking_list/<int:pk>/', BookingDetailView.as_view(), name = "booking_detail"),
]

app_name = "tickets"