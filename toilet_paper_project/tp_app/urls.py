from django.urls import path
from . import views

urlpatterns =[
    path('', views.tp_wall), 
    path('<int:request_session_user_id>/', views.user_page),
    path('tp/upload', views.upload)
]