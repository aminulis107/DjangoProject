from django.shortcuts import render
from django.http import HttpResponse

def first_app(request):
    return render(request,"base.html")

def page1(request):
    return render(request,"page1.html")

def compress(request):
    return render(request,"compress.html")

def convert(request):
    return render(request,"convert.html")

def merge(request):
    return render(request,"merge.html")