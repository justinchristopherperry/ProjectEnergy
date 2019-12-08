from django.db import models

class Member(models.Model):
    email = models.CharField(max_length=50, primary_key = True)
    name = models.CharField(max_length=50)

class Seller(models.Model):
    email = models.CharField(max_length=50, primary_key = True)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50)
    total_produced_2018_Gwh = models.FloatField(default=0.0)
    price_per_kwh = models.FloatField(default=0.0)

class Country(models.Model):
    name = models.CharField(max_length=50, primary_key = True)
    percent_pop_needs_elec = models.FloatField(default=0.0)




