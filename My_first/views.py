
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def login_sucess(request):
    return render(request,'login_sucess.html')


