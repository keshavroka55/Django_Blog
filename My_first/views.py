
from django.http import HttpResponse
from django.shortcuts import render
from keshav.models import Keshav 

def load(request):
    blogs = Keshav.objects.all().order_by('-created_at')
    return render (request, 'load.html',{'blogs':blogs})

def login_sucess(request):
    return render(request,'login_sucess.html')

def keshav_list(request):
    # q = request.GET.get('q') if request.GET.get('p') != None else ''
    # blogs = Keshav.objects.filter(category__icontains=q)

    blogs = Keshav.objects.all().order_by('-created_at')

    # user = Keshav.objects.all()
    context = {'blogs': blogs}
    return render(request, 'keshav_list.html', context)


