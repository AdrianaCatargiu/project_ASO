from django.contrib import admin

# Register your models here.
from scrumboard.models import List, Card
from .models import Room, Message
admin.site.register(List)
admin.site.register(Card)
admin.site.register(Room)
admin.site.register(Message)