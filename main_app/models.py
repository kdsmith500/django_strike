from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Location(models.Model):
    location_name = models.CharField(max_length=100)
    longitude = models.IntegerField()
    latitude = models.IntegerField()

    def __str__(self):
        return self.location_name

    def get_absolute_url(self):
        return reverse('locations_detail', kwargs={'pk': self.id})

class Weapon(models.Model):
    weapon_name = models.CharField(max_length=100)
    r_min = models.IntegerField()
    r_max = models.IntegerField()

    def __str__(self):
        return self.weapon_name

    def get_absolute_url(self):
        return reverse('weapons_detail', kwargs={'pk': self.id})
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    targets = models.CharField(max_length=250)
    money = models.IntegerField()
    strikes = models.IntegerField()
    strikes_recieved = models.IntegerField()
    weapons = models.ManyToManyField(Weapon)
    locations = models.ManyToManyField(Location)

    # def __str__(self):
    #     return self.user

    def get_absolute_url(self):
        return reverse('detail', kwargs={'profile_id': self.id})

class Base(models.Model):
    base_name = models.CharField(max_length=100)
    base_lat = models.IntegerField()
    base_lng = models.IntegerField()
    damage = models.IntegerField(blank=True, null=True)
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.base_name

    def get_absolute_url(self):
        return reverse('weapons_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['base_name',]