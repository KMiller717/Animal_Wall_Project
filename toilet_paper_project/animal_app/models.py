from django.db import models
from login_app.models import User

# Create your models here.
class Message(models.Model):
    tp_video = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, related_name = 'messages', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    message = models.ForeignKey(Message, related_name='comments', on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)