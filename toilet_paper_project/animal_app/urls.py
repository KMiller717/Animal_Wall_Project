from django.urls import path
from django.conf import settings
<<<<<<< HEAD
from . import views


=======
>>>>>>> 17be702278b83c50e2842ed809f0284bea9bcbc7
from . import views

urlpatterns =[
    path('<int:request_session_user_id>/', views.user_page),
    path('upload', views.upload),
    path('logout', views.logout),
    path('', views.video_wall), 
    path('video', views.post_video),
    path('<int:message_id>/delete', views.delete_post),
<<<<<<< HEAD
    path('<int:message_id>/comment', views.post_comment)
]
=======
    path('<int:message_id>/comment', views.post_comment),
    path('<int:request_session_user_id>/', views.user_page),
    path('upload', views.upload)
]

>>>>>>> 17be702278b83c50e2842ed809f0284bea9bcbc7
