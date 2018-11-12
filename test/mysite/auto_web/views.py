from django.shortcuts import render, HttpResponse
from auto_web import models
from django.db import connection
# Create your views here.


def t_view(request):
    print(request)

    return render(request, 'index.html')

user_list = []

def index(request):
    print(request)
    if request.method == 'POST':
        user = request.POST.get("user", None)
        password = request.POST.get("password", None)
        print(user, password)
        models.UserInfo.objects.create(user=user, password=password)
        # temp = {'username': username, 'password': password}
        # user_list.append(temp)
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html',{"data": user_list})

def login(request):

    return render(request, 'login.html')