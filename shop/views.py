from django.shortcuts import render
from django.http.response import HttpResponse



def Home(request):
    return HttpResponse("<h1>HOME</h1>")