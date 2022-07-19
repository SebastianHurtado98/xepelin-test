from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    if request.method == 'POST':
        username= request.POST["user"]
        password = request.POST["pass"]
    return render(request, 'login.html')

def index(request):
    return HttpResponse("You passed.")