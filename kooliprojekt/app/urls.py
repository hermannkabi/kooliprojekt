from django.urls import path
from . import views

urlpatterns = [
    path("ui/", views.ui, name="ui"),
    path("", views.index, name="index"),
    path("logout/", views.logout, name="signout"),
    path("register/", views.register, name="register"),
    path("course/<int:id>",views.course,name="course")
]