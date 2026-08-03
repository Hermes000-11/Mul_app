from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def bunker(request):
    return render(request, 'home.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room:room')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'registration_form.html', {'form': form})
