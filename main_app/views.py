from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def tutorial(request):
    return render(request, 'tutorial.html')

def profile(request):
    return render(request, 'profile.html')

def buy(request):
    return render(request, 'buy.html')