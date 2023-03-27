from django.shortcuts import render
from django.http import HttpResponse

def first_app(request):
    return render(request,"base.html")

def page1(request):
    return render(request,"page1.html")

