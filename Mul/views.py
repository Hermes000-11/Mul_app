from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required # decorator guard

def bunker(request):
    return render(request, 'home.html')
    #home page, simple html

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('room:room', room_name='default_room')
    else:
        form = UserCreationForm()
    # form = UserCreationForm() i dont know why i add this
    return render(request, 'registration_form.html', {'form': form})
# Ooops there is a bug, if user entered wrong password, it will not show the error message,
# just create a new form

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) 
        # request is http object, it can be POST or GET
        # and data(request.POST) is the data from the form, like username and password, it is a dictionary
        if form.is_valid():
            user = form.get_user() # return a user object from database, if it exists, otherwise return None

            auth_login(request, user) 
            # create a session for the user, and set the user as authenticated
            # and createn a cookie in the browser, so the user can be authenticated in the future requests
            
            return redirect('room:room', room_name='default_room') 
            # redirect to the default room after login
            # and pass the room_name as a parameter to the url in urls.py, and using it in the chat_show.html
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout(request):
    auth_logout(request)
    # clear the session and sessionid is not valid anymore
    return redirect('login')

@login_required(login_url='login')
# a decorator which checks if the user is authenticated,
# if not, redirect to the login page, and after login, redirect to chat room
def chat_room(request):
    return redirect('room:room', room_name='default_room')
