from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Location(models.Model):
    location_name = models.CharField(max_length=100)
    longitude = models.IntegerField()
    latitude = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('locations_detail', kwargs={'pk': self.id})

class Weapon(models.Model):
    weapon_name = models.CharField(max_length=100)
    r_min = models.IntegerField()
    r_max = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('weapons_detail', kwargs={'pk': self.id})
        
class User(models.Model):
    user = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    bio = models.TextField(max_length=250)
    base = models.CharField(max_length=100)
    satellite = models.CharField(max_length=250)
    targets = models.CharField(max_length=250)
    money = models.IntegerField()
    strikes = models.IntegerField()
    strikes_recieved = models.IntegerField()
    weapons = models.ManyToManyField(Weapon)
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'user_id': self.id})
