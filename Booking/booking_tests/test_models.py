from django.test import TestCase
from django.contrib.auth.models import User
from Booking.models import TravelOption, Booking
from django.utils import timezone
from datetime import timedelta

class TravelOptionModelTest(TestCase):
    def setUp(self):
        self.travel = TravelOption.objects.create(
            type="Bus",
            source="City A",
            destination="City B",
            date_time=timezone.now() + timedelta(days=1),  # timezone-aware
            price=500,
            available_seats=30
        )

    def test_travel_option_creation(self):
        self.assertEqual(self.travel.source, "City A")
        self.assertEqual(self.travel.destination, "City B")
        self.assertEqual(self.travel.available_seats, 30)
        self.assertEqual(str(self.travel), f"{self.travel.type} from {self.travel.source} to {self.travel.destination}")


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.travel = TravelOption.objects.create(
            type="Train",
            source="City X",
            destination="City Y",
            date_time=timezone.now() + timedelta(days=2),  # timezone-aware
            price=1000,
            available_seats=50
        )
        self.booking = Booking.objects.create(
            user=self.user,
            travel_option=self.travel,
            number_of_seats=2,
            total_price=2000,
            status="Confirmed"  # ensure status exists if used in __str__ or views
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.user.username, "testuser")
        self.assertEqual(self.booking.number_of_seats, 2)
        self.assertEqual(self.booking.total_price, 2000)
        self.assertEqual(self.booking.travel_option.source, "City X")
        # Use booking.pk instead of id in __str__ to avoid None before save
        self.assertEqual(str(self.booking), f"Booking {self.booking.pk} by {self.booking.user.username}")
