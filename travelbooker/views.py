from django.shortcuts import render
from Booking.models import TravelOption  # import TravelOption from Booking app

def home(request):
    """Main website landing page with featured travel options"""
    featured_travels = TravelOption.objects.order_by('date_time')[:3]
    return render(request, "index.html", {"featured_travels": featured_travels})


