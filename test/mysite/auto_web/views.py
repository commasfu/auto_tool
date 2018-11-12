from django.shortcuts import render, HttpResponse
from auto_web import models
# Create your views here.


def t_view(request):
    print(request)

    return render(request, 'index.html')

user_list = []

def index(request):
    print(request)
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)
        models.UserInfo.objects.create(user=username, password=password)
        # temp = {'username': username, 'password': password}
        # user_list.append(temp)
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html',{"data": user_list})