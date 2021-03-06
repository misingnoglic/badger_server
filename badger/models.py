from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Location(models.Model):
    house_number = models.PositiveSmallIntegerField()
    street = models.CharField(max_length = 70)
    city = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)
    rating = models.PositiveSmallIntegerField()
    verified = models.BooleanField()
    votes = models.IntegerField()
    image = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, default=None, null=True)

    def __str__(self):
        return self.name

class Badge(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location)
    description = models.CharField(max_length=200)
    points = models.PositiveSmallIntegerField()
    verified = models.BooleanField()
    votes = models.IntegerField()
    image = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category,default=None, null=True)
    def __str__(self):
        return self.name


class BadgerUser(models.Model):
    user = models.OneToOneField(User)
    badges = models.ManyToManyField(Badge)
    image = models.URLField(null=True)
    def __str__(self):
        return self.user.username

