from django.urls import path, re_path
from . import views 
app_name = 'room'
urlpatterns = [
    path('<str:room_name>/', views.room, name='room'),
]

# nothing to explain tbh, but views.py process and render html template
