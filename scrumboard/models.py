from django.db import models
from datetime import datetime
# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=50)


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # relation with foreign key bellow
    # EACH Card must belong to list
    list = models.ForeignKey(List, related_name="cards", on_delete=models.CASCADE)
    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)

class Room(models.Model):
    name= models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)