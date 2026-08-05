from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def bunker(request):
    return render(request, 'home.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room:room', room_name='default_room')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'registration_form.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            from django.contrib.auth import login
            user = form.get_user()
            login(request, user)
            return redirect('room:room', room_name='default_room')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
