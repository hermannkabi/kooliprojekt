from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as django_logout, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    try:
        return dictionary.get(key, "")
    except:
        return ""


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "homepage.html")
    
    return render(request, "dashboard.html")
    

def ui(request):
    return render(request, "ui_components.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")

    else:
        form = UserCreationForm()

    context = {"form":form}
    return render(request, "registration/register.html", context)


def logout(request):
    django_logout(request)
    return redirect("/")
