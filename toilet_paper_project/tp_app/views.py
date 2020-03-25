from django.shortcuts import render, redirect 
from .models import Message, Comment
from login_app.models import User

# Create your views here.

def tp_wall(request):
    return render(request, "tp_wall.html")