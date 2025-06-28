
from django.http import HttpResponse
from django.shortcuts import render
from keshav.models import Keshav

def load(request):
    blogs = Keshav.objects.all().order_by('-created_at')
    return render (request, 'load.html',{'blogs':blogs})

def home(request):
    return render(request,'home.html')

def login_sucess(request):
    return render(request,'login_sucess.html')

def keshav_list(request):
    blogs = Keshav.objects.all().order_by('-created_at')
    return render(request, 'keshav_list.html', {'blogs': blogs})


