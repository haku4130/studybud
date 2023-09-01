from django.shortcuts import render

from .models import Room


def index(request):
    template = 'index.html'
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, template, context)


def room(request, id):
    template = 'room.html'
    room = Room.objects.get(id=id)
    context = {'room': room}
    return render(request, template, context)
