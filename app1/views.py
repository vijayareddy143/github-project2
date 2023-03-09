from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def jaga(request):
    return HttpResponse('<h1>he is very good person</h1>')