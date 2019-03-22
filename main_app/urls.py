from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('create/', views.BaseCreate.as_view(), name='base_create'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('profile/', views.profile, name='profile'),
    path('buy/', views.buy, name='buy'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]