from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def helloWorld(request):
    now = datetime.datetime.now()
    return render(request, "accueil/helloWorld.html", context={"temps":now})

def sum(request, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    somme =  num1 + num2
    return render(request, "accueil/sum.html", context={'somme': somme, 'num1':num1, 'num2':num2})