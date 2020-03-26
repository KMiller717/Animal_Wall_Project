from django.shortcuts import render, redirect 
from .models import Message, Comment
from login_app.models import User





def tp_wall(request):
    return render(request, "animal_wall.html")

def user_page(request, request_session_user_id) :
    context ={
        'user': User.objects.get(id=request.session['user_id']),
        'messages': Message.objects.all()
    }
    return render (request, 'user_page.html', context)

def upload(request):
    user_to_update= User.objects.get(id=request.session['user_id'])
    print(request.FILES)
    user_to_update.user_image = request.FILES['user_image']
    user_to_update.save()
    return redirect(f'/tp/{user_to_update.id}')   

def logout(request):
    del request.session['user_id']
    del request.session['user_first_name']
    del request.session['user_email']
    return redirect ('/')

def view_wall(request):
    return render(request, "tp_wall.html")