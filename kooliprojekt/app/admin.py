from django.contrib import admin
from .models import Course,Lesson,LessonCompleted, Question
# Register your models here.


class LessonAdmin(admin.ModelAdmin):
        list_display = ["title", "course", "lessonNumber", "onlyForAdmin"]

admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonCompleted)
admin.site.register(Question)