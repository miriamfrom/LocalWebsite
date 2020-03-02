from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=40)
    #flag = models.ImageField(upload_to='flags', blank=True, null=True)


class Continent(models.Model):
    countries = models.ManyToManyField(Country)


class Map(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)