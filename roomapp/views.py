from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from roomapp.models import Room, Message


# Create your views here.
class RoomsView(ListView):
    model = Room
    template_name = 'roomapp/rooms.html'
    context_object_name = 'rooms'
    page_kwarg = 'page'


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'roomapp/room.html', {'room': room, 'messages': messages})
