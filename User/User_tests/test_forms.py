from django.test import TestCase
from django.contrib.auth.models import User
from User.forms import UserProfileForm

class UserProfileFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")

    def test_valid_form(self):
        form_data = {
            "username": "testuser",  # required
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com"
        }
        form = UserProfileForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        form_data = {
            "username": "testuser",
            "first_name": "John",
            "last_name": "Doe",
            "email": "invalid-email"
        }
        form = UserProfileForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

