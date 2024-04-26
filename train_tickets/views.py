from django.shortcuts import render, redirect
from train_tickets.models import *
from train_tickets.forms import PlaceAdd, TicketAdd
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class PlaceListView(ListView):
    model = Place
    context_object_name = "places"
    template_name = "tickets/place_list.html"


class PlaceDetailView(DetailView):
    model = Place
    template_name = "tickets/place_detail.html"
    context_object_name = "place"

class PlaceAddView(CreateView):
    model = Place
    template_name = "tickets/place_add.html"
    form_class = PlaceAdd
    success_url = "/"

class BookingAddView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = "tickets/booking_add.html"
    form_class = TicketAdd
    success_url = "/"

class BookingListView(ListView):
    model = Booking
    context_object_name = "bookings"
    template_name = "tickets/booking_list.html"

class BookingDetailView(DetailView):
    model = Booking
    template_name = "tickets/booking_detail.html"
    context_object_name = "booking"