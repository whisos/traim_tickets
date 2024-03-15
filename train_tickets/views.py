from django.shortcuts import render, redirect
from train_tickets.models import *
from django.http import HttpResponse


def index(request):
    places = Place.objects.all()
    context = {"places":places}
    return render(request, "train_tickets/index.html", context=context)


def place_detail(request, place_id):
    place = Place.objects.get(id=place_id)
    context = {"place":place}
    return render(request, "train_tickets/detail.html", context=context)

def place_form(request, place_id):
    if request.method == "POST":
        date = request.POST.get("train_date")
        time = request.POST.get("train_time")
        booking = Booking.objects.create(
          place=Place.objects.get(id=place_id),
          date=date,
          time=time
        )
        return redirect("booking_details", pk=booking.id)
    else:
        return render(request, template_name="train_tickets/place_form.html", context={"place_id": place_id})

def booking_details(request, pk):
    try:
        booking = Booking.objects.get(id=pk)
        context = {
            "booking": booking
        },
        return render(request, template_name="booking/booking_details.html", context=context)
    except Booking.DoesNotExist:
        return HttpResponse(
            "This booking doesn't exist",
            status=404
        )