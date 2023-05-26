from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, logout as django_logout, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.template.defaulttags import register
from .models import Course, Lesson,LessonCompleted, Question, QuestionChoice
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import re, random, math

@register.filter
def get_item(dictionary, key):
    try:
        return dictionary.get(key, "")
    except:
        return ""
    
@register.filter
def progress(course, user):
    lessons_completed = LessonCompleted.objects.filter(Q(lesson__course = course) & Q(user = user))
    total_lessons = Lesson.objects.filter(course = course)
    if len(total_lessons) <= 0:
        return "0%"
    percent = round((len(lessons_completed)/len(total_lessons))*100)
    return str(percent) + "%"

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "homepage.html")
    context = {}
    courses=Course.objects.filter(kasutajad = request.user)
    context["courses"] = courses
    context["message"] = request.session.get("message", None)

    #Clears the message so that it will not appear on refresh
    request.session["message"] = None
    return render(request, "dashboard.html",context)


def ui(request):
    return render(request, "ui_components.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data['password1']
            email = request.POST["email"]
            user = authenticate(username=username, password=password)
            user.email = email
            user.save()
            login(request, user)
            return redirect("index")

    else:
        form = UserCreationForm()

    context = {"form":form}
    return render(request, "registration/register.html", context)


def logout(request):
    django_logout(request)
    return redirect("/")


@login_required
def course(request, id):

    course = get_object_or_404(Course, pk=id)

    if not course.kasutajad.contains(request.user):
        request.session["message"] = "Sul ei ole õigust sellele lehele ligi pääseda"
        return redirect("/")

    lessons = Lesson.objects.filter(course__id=id).order_by("lessonNumber")
    if not request.user.is_superuser:
        lessons = lessons.filter(onlyForAdmin = False)
    completed = LessonCompleted.objects.filter(Q(user=request.user) & Q(lesson__in=lessons))
    context = {}
    context["lessons"] = lessons
    context["completed"] = completed
    context["completedLessons"] = [x.lesson for x in completed]
    context["course"] = Course.objects.get(pk=id)

    return render(request, "course.html",context)

@login_required
def lesson(request, id):
    

    context = {}

    lesson = get_object_or_404(Lesson, pk=id)

    if not lesson.course.kasutajad.contains(request.user) or lesson.onlyForAdmin and not request.user.is_superuser:
        request.session["message"] = "Sul ei ole õigust sellele lehele ligi pääseda"
        return redirect("/")


    is_complete = None
    try:
        is_complete = LessonCompleted.objects.get(Q(user=request.user) & Q(lesson=lesson))
    except:
        is_complete = None

    context["lesson"] = lesson
    context["course"] = lesson.course
    context["isComplete"] = is_complete is not None

    return render(request, "lessons/"+str(lesson.course.id)+"/"+lesson.lesson+".html", context)


@login_required
def finishLesson(request, id):
    lesson_completed = LessonCompleted(user = request.user, lesson = get_object_or_404(Lesson, pk=id))
    lesson_completed.save()
    return redirect("/")

@login_required
def addCourse(request):
    not_owned_by_user = Course.objects.all().exclude(kasutajad=request.user)
    context = {}

    context["all_courses"] = not_owned_by_user
    return render(request, "add.html", context)


@login_required
def coursePreview(request, id):

    course = get_object_or_404(Course, pk=id)

    if course.kasutajad.contains(request.user):
        # Don't show the preview, redirect to the course content
        return redirect("course", id=id)

    lessonCount = len(Lesson.objects.filter(course=course))

    context = {}
    context["course"] = course
    context["lessonCount"] = lessonCount
    return render(request, "course_preview.html", context)


@login_required
def registerToCourse(request, id):
    course = get_object_or_404(Course, pk=id)

    if course.kasutajad.contains(request.user):
        return redirect("/")
    
    course.kasutajad.add(request.user)

    return redirect("/")


def view_not_found(request, exception):
    return render(request, "404.html")


@login_required
def profile(request):
    #Message handling
    message = request.session["message"]
    request.session["message"] = None

    #Write additional user data code here

    return render(request, "profile.html", {"user":request.user, "message":message})

def generate_random_float(a, b, c):
    random_int = random.randint(math.ceil(a / c), math.floor(b / c))
    random_float = random_int * c
    return int(random_float) if random_float.is_integer() else round(random_float, 2)


def exercise(request, id):
    question = get_object_or_404(Question, pk=id)
    choices = QuestionChoice.objects.filter(question=question)

    pattern = r"##([\d.,]+)##"

    context = {}

    context["question"] = question
    context["choices"] = choices
    context["show_round"] = False


    text = question.explanation + question.question + question.explanation
    numbers = re.findall(pattern, text)
    if len(numbers) > 0:
        individual_numbers = numbers[0].split(',')
        random_data = generate_random_float(float(individual_numbers[0]), float(individual_numbers[1]), float(individual_numbers[2]))
        random_answer = eval(question.constant)
        random_answer = int(random_answer) if random_answer.is_integer() else round(random_answer, 2)
        question.question = re.sub(pattern, str(random_data).replace(".", ","), question.question)
        question.description = re.sub(pattern, str(random_data).replace(".", ","), question.description)
        question.explanation = re.sub(pattern, str(random_data).replace(".", ","), question.explanation)
        question.explanation = question.explanation.replace("##answer##", str(random_answer).replace(".", ","))
        correct_choice = QuestionChoice(answer=str(random_answer), is_correct=True)
        correct_choice2 = QuestionChoice(answer=str(random_answer).replace(".", ","), is_correct=True)
        question.min = 0
        question.max = (random_answer // 100 + 1)*100
        question.correct_min = math.floor(random_answer)
        question.correct_max = math.ceil(random_answer)

        context["choices"] = [correct_choice, correct_choice2]
        context["show_round"] = True


    return render(request, "exercise.html", context)

@login_required
def saveUserData(request, username, email):
    try:
        user = request.user
        user.username = username

        if email != "none":
            user.email = email

        user.save()
    except:
        request.session['message'] = "Andmeid ei saanud uuendada!"
    return redirect("profile")