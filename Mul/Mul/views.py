from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def bunker(request):
    return render(request, 'home.html')

def registration(request):
    form = UserCreationForm()
    return render(request, 'registration_form.html', {'form': form})
