from django.shortcuts import render, HttpResponse, redirect

def index(req):
    response = "Hello, I am your first request!"
    return HttpResponse(response)
    # return render(req, 'myapp/index.html')

def index2(req):
    return render(req, 'myapp/index.html')