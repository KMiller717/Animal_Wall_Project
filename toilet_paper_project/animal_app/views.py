from django.shortcuts import render, redirect 
from .models import Message, Comment
from login_app.models import User
import tweepy
from datetime import date, timedelta


consumer_key= 'Nllt36ILNQs04HHHqYp8U2VgQ'
consumer_secret= '10NY6qMnhLMOc2vkjOlfgJu96v3Sp4WlrqSA4RcIBdjD9yQvpx'
access_token= '775701192169127936-HHpPy1eNdngnfLxCmosyfKcNSG27ItS'
access_token_secret= 'KwcqoiH44KdDpndpjCWFIpVitWtmLa2vQYD0dDKFH6UuW'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


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
    return redirect(f'/wall/{user_to_update.id}')   

def logout(request):
    del request.session['user_id']
    del request.session['user_first_name']
    del request.session['user_email']
    return redirect ('/')



def view_wall(request):
    return redirect('/wall')

# Create your views here.

def video_wall(request):
    yesterday = date.today() - timedelta(days=1)
    tweets = tweepy.Cursor(api.search, q = 'dogs', lang='en', since = yesterday).items(10)
    urls = []
    for tweet in tweets:
        urls.append('https://twitter.com/x/status/' + tweet.id_str)

    context= {
        'urls': urls,
        'all_messages': Message.objects.all()
    }
    return render(request, "animal_wall.html", context)

def post_video(request):
    
    user = User.objects.get(id=request.session['user_id'])
    video = request.POST['video'][-11:]
    print(video)
    message = Message.objects.create(tp_video=video, description=request.POST['description'], user=user)

    return redirect('/wall')

def delete_post(request, message_id):
    post_delete = Message.objects.get(id=message_id)
    post_delete.delete()

    return redirect('/wall')

def post_comment(request, message_id):
    
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=message_id)
    comment = Comment.objects.create(
        content=request.POST['comment'], 
        message=message,
        user=user
    )
    print(comment)

    return redirect('/wall')
