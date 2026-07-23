from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def room(request, room_name):
    return render(request, 'room/chat_show.html', {'room_name': room_name})