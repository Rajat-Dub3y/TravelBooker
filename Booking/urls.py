from django.urls import path
from . import views

app_name = "Booking"   # 👈 very important for namespaced URLs

urlpatterns = [
    path("", views.travel_list, name="travel_list"),
    path("travel/<int:pk>/", views.travel_detail, name="travel_detail"),
    path("book/<int:pk>/", views.book_travel, name="book_travel"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path("cancel-booking/<int:pk>/", views.cancel_booking, name="cancel_booking"),
]
