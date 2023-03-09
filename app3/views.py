from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def narendra(request):
    return HttpResponse('<h1><marquee>Narendra is very good frd of mine</h1></marquee>')

def vijji(request):
    return HttpResponse('<h1><marquee>Vijji is very cute girl </h1></marquee>')