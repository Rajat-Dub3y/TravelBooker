from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout
import time
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm,SignupForm,SigninForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect("auth:signin")
    else:
        form = SignupForm()

    return render(request, "auth/signup.html", {"form": form})


def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Signed in successfully.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = SigninForm()

    return render(request, "auth/signin.html", {"form": form})

    

def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('auth:signin')   # redirect instead of render

@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('auth:profile')  # <-- should redirect
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, "auth/profile.html", {"form": form})


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()  # saves the new password
            update_session_auth_hash(request, user)  # keeps the user logged in
            messages.success(request, "Your password was successfully updated!")
            return redirect('auth:profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, "auth/change_password.html", {"form": form})
