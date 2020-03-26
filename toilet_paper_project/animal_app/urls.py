from django.urls import path
from . import views

urlpatterns =[
    path('', views.video_wall), 
    path('video', views.post_video),
    path('<int:message_id>/delete', views.delete_post),
    path('<int:message_id>/comment', views.post_comment)
]