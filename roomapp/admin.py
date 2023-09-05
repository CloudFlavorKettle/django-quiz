from django.contrib import admin

from roomapp.models import Room, Message

# Register your models here.
admin.site.register(Room)

admin.site.register(Message)