from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Location, Weapon
import uuid
import boto3

def home(request):
  return render(request, 'home.html')

def main(request):
  return render(request, 'main.html')

def tutorial(request):
  return render(request, 'tutorial.html')

def profile(request):
  return render(request, 'profile.html')

def buy(request):
  return render(request, 'buy.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid credentials - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)