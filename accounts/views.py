from django.shortcuts import render

import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm_pass = request.POST.get('password2')

        if password == confirm_pass:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User already exists")
                return redirect("/")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Account created successfully")
                return redirect("signin")

        else:
            messages.error(request, "Confim Password incorrect")
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "User has been signed in successfully")
            return redirect("profile")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'signin.html')


def profile(request):
    return render(request, 'profile.html')


def signout(request):
    logout(request)
    messages.error(request, "User has been signed out successfully")
    return redirect("signin")

