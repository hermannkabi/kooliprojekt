from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('exercise/<str:question>', views.exercise, name='exercise'),

]