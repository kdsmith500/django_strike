from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Location, Weapon, Base
import uuid
import boto3

class BaseCreate(LoginRequiredMixin, CreateView):
  model = Base
  fields = ['base_name', 'base_lat', 'base_lng']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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

def signup(request, user_id):
  user = User.objects.get(pk=user_id)
  user.save()
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

# def registration(request):
#   user = request.user
#   return render(request, 'registration/registration.html', {'form': ProfileForm})

# def create_profile(request):
#   error_message = ''
#   if request.method == 'POST':
#     # user_form = UserCreationForm(request.POST, instance=request.user)
#     profile_form = ProfileForm(request.POST)
#     print('Made it past user_form & profile_form')
#     if profile_form.is_valid():
#       print('Forms have been validated')
#       new_profile = profile_form.save(commit=False)
#       new_profile.user = request.user
#       print('new_profile.user = request.user is working')
#       # print(profile_form)
#       profile_form.save()
#       print(profile_form.save())
#     else:
#       msg = 'Errors: %s' % profile_form.errors.as_text()
#       print(msg)  
#   else:
#     print('We are hitting the redirect')
#     user_form = UserCreationForm(instance=request.user)
#     profile_form = ProfileForm(instance=request.user.profile)
#   return redirect('index')