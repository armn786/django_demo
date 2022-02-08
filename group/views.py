from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def group(request):
    return HttpResponse("group called.....")

def index(request):
    return render(request,'group/index.html')

def contactUs(request):
    return render(request,'group/contactUs.html')

def aboutUs(request):
    return render(request,'group/aboutUs.html')

