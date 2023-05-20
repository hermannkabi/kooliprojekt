from django.urls import path
from . import views

urlpatterns = [
    path("ui/", views.ui, name="ui"),
    path("", views.index, name="index"),
    path("logout/", views.logout, name="signout"),
    path("register/", views.register, name="register"),
    path("course/<int:id>",views.course,name="course"),
    path("lesson/<int:id>", views.lesson, name="lesson"),
    path("finishLesson/<int:id>", views.finishLesson, name="finishLesson"),
    path("course/add", views.addCourse, name="addCourse"),
    path("course/<int:id>/preview", views.coursePreview, name="coursePreview"),
    path("course/<int:id>/enroll", views.registerToCourse, name="registerToCourse"),
    
    
]