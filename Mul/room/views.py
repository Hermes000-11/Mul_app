from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def room(request, room_name):
    return render(request, 'room/chat_show.html', {'room_name': room_name})

def registration(request):
    form = UserCreationForm()
    return render(request, 'room/registration_form.html', {'form': form})