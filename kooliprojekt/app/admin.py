from django.contrib import admin
from .models import Course,Lesson,LessonCompleted, Question
# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(LessonCompleted)
admin.site.register(Question)