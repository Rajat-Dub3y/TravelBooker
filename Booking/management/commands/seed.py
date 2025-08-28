from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Booking.models import TravelOption, Booking
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **kwargs):
        # --- Create test users ---
        if not User.objects.filter(username="testuser").exists():
            user = User.objects.create_user(username="testuser", password="password123")
            self.stdout.write(self.style.SUCCESS("Created test user: testuser"))
        else:
            user = User.objects.get(username="testuser")
            self.stdout.write("Test user already exists.")

        # --- Create travel options ---
        travel_data = [
            {
                "type": "Bus",
                "source": "Kolkata",
                "destination": "Delhi",
                "price": 1200,
                "available_seats": 40,
                "date_time": timezone.now() + timedelta(days=1)  # tomorrow
            },
            {
                "type": "Flight",
                "source": "Kolkata",
                "destination": "Mumbai",
                "price": 5000,
                "available_seats": 100,
                "date_time": timezone.now() + timedelta(days=2)
            },
            {
                "type": "Train",
                "source": "Haldia",
                "destination": "Patna",
                "price": 900,
                "available_seats": 200,
                "date_time": timezone.now() + timedelta(days=3)
            },
            {
                "type": "Flight",
                "source": "Delhi",
                "destination": "Bangalore",
                "price": 4500,
                "available_seats": 120,
                "date_time": timezone.now() + timedelta(days=4)
            },
            {
                "type": "Bus",
                "source": "Patna",
                "destination": "Kolkata",
                "price": 800,
                "available_seats": 50,
                "date_time": timezone.now() + timedelta(days=5)
            },
]

        for data in travel_data:
            obj, created = TravelOption.objects.get_or_create(**data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added travel: {obj}"))
            else:
                self.stdout.write(f"Travel already exists: {obj}")

        # --- Optionally, create a sample booking ---
        if not Booking.objects.filter(user=user).exists():
            travel = TravelOption.objects.first()
            booking = Booking.objects.create(
                user=user,
                travel_option=travel,
                number_of_seats=2,
                total_price=2 * travel.price,
                booking_date=timezone.now(),
                status="Confirmed"
            )
            self.stdout.write(self.style.SUCCESS(f"Created sample booking for user {user.username}"))
        else:
            self.stdout.write("Sample booking already exists.")

        self.stdout.write(self.style.SUCCESS("Database seeded successfully ✅"))
