from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def commas(request):
    return HttpResponse('付成祥，hello!')

def blogs(request):
    return render(request, 'home.html')