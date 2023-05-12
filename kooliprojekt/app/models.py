from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length = 200)
    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class LessonCompleted(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.lesson

class Question(models.Model):
    question = models.CharField(max_length=200)
    def __str__(self):
        return self.question