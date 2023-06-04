from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length = 200)
    kasutajad = models.ManyToManyField(User)
    image = models.TextField(blank=True, default="https://images.theconversation.com/files/191827/original/file-20171025-25516-g7rtyl.jpg?ixlib=rb-1.1.0&rect=0%2C70%2C7875%2C5667&q=45&auto=format&w=926&fit=clip")
    description = models.TextField(default="Kirjeldus selle kursuse kohta")
    only_for_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.CharField(max_length=200)
    image = models.TextField(blank=True, default="https://previews.123rf.com/images/tupungato/tupungato1612/tupungato161200137/69249841-physics-lesson-hand-written-law-of-physics-equations-set-science-vector-illustration.jpg")
    onlyForAdmin = models.BooleanField(default=False)
    lessonNumber = models.PositiveSmallIntegerField(default=1)
    def __str__(self):
        return self.title

class LessonCompleted(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.lesson)

class Question(models.Model):
    question = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    type = models.CharField(max_length=50, default="one")
    # WARNING! This field is rendered as safe, meaning that putting HTML here is a really bad idea
    explanation = models.TextField(default="", blank=True)
    image = models.TextField(blank=True)
    # These are only effective, if type=range
    correct_min = models.PositiveSmallIntegerField(blank=True, default=0)
    correct_max = models.PositiveSmallIntegerField(blank=True, default=10)
    # This is used only when the data is randomized
    # The content is simply Python code, that can access the random_data variable to make an equation
    constant = models.CharField(default="random_data", max_length=255)
    unit = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.question


class QuestionChoice(models.Model):
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer