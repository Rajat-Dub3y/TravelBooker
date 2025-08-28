from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TravelOption, Booking
from .forms import BookingForm
from django.db.models import Q
from datetime import datetime

from django.utils.dateparse import parse_date

def travel_list(request):
    """List all available travel options with advanced filters"""
    travel_type = request.GET.get("type")
    source = request.GET.get("source")
    destination = request.GET.get("destination")
    date = request.GET.get("date")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    min_seats = request.GET.get("min_seats")

    travels = TravelOption.objects.all()

    if travel_type:
        travels = travels.filter(type=travel_type)
    if source:
        travels = travels.filter(source__icontains=source)
    if destination:
        travels = travels.filter(destination__icontains=destination)
    if date:
        travels = travels.filter(date_time__date=date)
    if min_price:
        travels = travels.filter(price__gte=min_price)
    if max_price:
        travels = travels.filter(price__lte=max_price)
    if min_seats:
        travels = travels.filter(available_seats__gte=min_seats)

    return render(request, "Booking/travel_list.html", {"travels": travels})


def travel_detail(request, pk):
    """View details of a travel option"""
    travel = get_object_or_404(TravelOption, pk=pk)
    return render(request, "Booking/travel_detail.html", {"travel": travel})


@login_required
def book_travel(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)

    if request.method == "POST":
        seats = int(request.POST.get("number_of_seats", 1))
        if seats <= travel.available_seats:
            booking = Booking.objects.create(
                user=request.user,
                travel_option=travel,
                number_of_seats=seats,
                total_price=seats * travel.price,
                status="Confirmed"
            )
            travel.available_seats -= seats
            travel.save()
            messages.success(request, "Booking confirmed!")
            return redirect("Booking:my_bookings")
        else:
            messages.error(request, "Not enough seats available.")

    # Always return a response
    return render(request, "Booking/book_travel.html", {"travel": travel})


@login_required
def my_bookings(request):
    """List current user's bookings"""
    bookings = Booking.objects.filter(user=request.user).order_by("-booking_date")
    return render(request, "Booking/my_bookings.html", {"bookings": bookings})


@login_required
def cancel_booking(request, pk):
    """Cancel a booking"""
    booking = get_object_or_404(Booking, pk=pk, user=request.user)

    if booking.status == "Confirmed":
        booking.status = "Cancelled"
        booking.save()

        booking.travel_option.available_seats += booking.number_of_seats
        booking.travel_option.save()

        messages.success(request, "Booking cancelled successfully!")
    else:
        messages.warning(request, "This booking is already cancelled.")

    return redirect("Booking:my_bookings")
