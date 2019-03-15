from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Herro /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def strike_index(request):
    return render(request, 'strike/index.html', { 'strike': strike })
