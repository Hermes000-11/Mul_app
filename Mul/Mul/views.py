from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def bunker(request):
    return render(request, 'home.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('room:room', room_name='default_room')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'registration_form.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('room:room', room_name='default_room')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
def chat_room(request):
    return render(request, 'chat_show.html')
