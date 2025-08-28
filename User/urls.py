from django.urls import path
from . import views

app_name = "auth"  # must match the namespace used in templates and redirects

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("change-password/", views.change_password, name="change_password")
]
