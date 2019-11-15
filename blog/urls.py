from django.urls import path
from . import views

urlpattrens = [
    path('', views.post_list, name='post_list')
]