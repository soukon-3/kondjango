# hello/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('bye/', views.bye_world, name='bye_world'),
]
