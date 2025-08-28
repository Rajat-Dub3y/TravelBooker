from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from Booking.models import TravelOption, Booking
from django.utils import timezone
from datetime import timedelta

class TravelViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")

        # Use timezone-aware datetime to avoid warnings
        self.travel = TravelOption.objects.create(
            type="Flight",
            source="City A",
            destination="City B",
            date_time=timezone.now() + timedelta(days=1),
            price=1000,
            available_seats=10
        )

    def test_travel_list_view(self):
        url = reverse("Booking:travel_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "City A")

    def test_travel_detail_view(self):
        url = reverse("Booking:travel_detail", args=[self.travel.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "City B")

    def test_book_travel_requires_login(self):
        url = reverse("Booking:book_travel", args=[self.travel.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # redirected to login

    def test_book_travel_authenticated(self):
        self.client.login(username="testuser", password="12345")
        url = reverse("Booking:book_travel", args=[self.travel.pk])
        response = self.client.get(url)
        # Make sure view returns HttpResponse
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Book")

    def test_my_bookings_view_requires_login(self):
        url = reverse("Booking:my_bookings")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_cancel_booking(self):
        self.client.login(username="testuser", password="12345")
        booking = Booking.objects.create(
            user=self.user,
            travel_option=self.travel,
            number_of_seats=1,
            total_price=1000,
            status="Confirmed"  # explicitly set status
        )
        url = reverse("Booking:cancel_booking", args=[booking.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        booking.refresh_from_db()
        self.assertEqual(booking.status, "Cancelled")
