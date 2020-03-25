from django.shortcuts import render, redirect 
from .models import Message, Comment
from login_app.models import User


# Create your views here.

def tp_wall(request):
    return render(request, "tp_wall.html")

def user_page(request, request_session_user_id) :
    context ={
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render (request, 'user_page.html', context)

def upload(request):
    print(request.FILES)
    User.objects.create(user_image = request.FILES['image'])
    return redirect('/tp/{request.session.user_id}')