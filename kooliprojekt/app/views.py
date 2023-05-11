from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "app/index.html")


def exercise(request, question):
    # Add some logic here
    return render(request, "app/test.html", {"question":question})