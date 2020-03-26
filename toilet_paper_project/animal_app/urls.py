from django.urls import path
from django.conf import settings
from . import views


urlpatterns =[
    path('<int:request_session_user_id>/', views.user_page),
    path('upload', views.upload),
    path('logout', views.logout),
    path('', views.video_wall), 
    path('video', views.post_video),
    path('<int:message_id>/delete', views.delete_post),
    path('<int:message_id>/comment', views.post_comment)
]

