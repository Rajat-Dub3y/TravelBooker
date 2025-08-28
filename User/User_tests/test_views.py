from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UserViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")

    def test_profile_view_requires_login(self):
        url = reverse("auth:profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_profile_update(self):
        self.client.login(username="testuser", password="12345")
        url = reverse("auth:profile")
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            # include any required fields in UserProfileForm
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) 
