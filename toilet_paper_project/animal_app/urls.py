from django.urls import path
from django.conf import settings

from . import views

urlpatterns =[
    path('', views.tp_wall), 
    path('<int:request_session_user_id>/', views.user_page),
    path('upload', views.upload),
    path('logout', views.logout),
]

