from django.urls import path
from . import views

urlpatterns = [
    path("ui/", views.ui, name="ui"),
    path("", views.index, name="index"),
    path("logout/", views.logout, name="signout"),
    path("register/", views.register, name="register"),
    path("course/<int:id>",views.course,name="course"),
    path("lesson/<int:id>", views.lesson, name="lesson"),
    #PLEASE don't change that
    path("finishLesson/<int:id>", views.finishLesson, name="finishLesson"),
    path("course/add", views.addCourse, name="addCourse"),
    path("course/<int:id>/preview", views.coursePreview, name="coursePreview"),
    path("course/<int:id>/enroll", views.registerToCourse, name="registerToCourse"),
    # path("user/<str:username>", views.profile, name="profile"),
    path("profile", views.profile, name="profile"),
    path("save/user/data/<str:username>/<str:email>", views.saveUserData, name="saveUserData"),
    path("exercise/<int:id>", views.exercise, name="exercise"),
    path("lesson/<int:id>/remove", views.removeLesson, name="removeLesson"),
    path("profile/manage", views.manageCourses, name="manageCourses"),
    path("profile/manage/<int:id>", views.manageCourse, name="manageCourse"),
    path("remove/<int:id>", views.removeCourse, name="removeCourse"),
    path("delete/account", views.deleteAccount, name="deleteAccount"),

    
]