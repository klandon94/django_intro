from django.shortcuts import render, redirect
from time import strftime


def index(request):
    data = {
        "date": strftime("%B %d, %Y"), # automatically adds localtime() as parameter
        "time": strftime("%I:%M %p")
    }
    return render(request,'myapp/index.html', data)