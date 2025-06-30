
from django.http import HttpResponse
from django.shortcuts import render
from keshav.models import Keshav 

def load(request):
    blogs = Keshav.objects.all().order_by('-created_at')
    return render (request, 'load.html',{'blogs':blogs})

def login_sucess(request):
    return render(request,'login_sucess.html')

def keshav_list(request):
    blogs = Keshav.objects.all().order_by('-created_at')
    context = {'blogs': blogs}
    return render(request, 'keshav_list.html', context)

# for search features.
def keshav_list(request):
    category = request.GET.get('category')  # ?category=TRAVEL
    username = request.GET.get('username')  # ?username=john

    blogs = Keshav.objects.all()

    # Filter by category if provided
    if category:
        blogs = blogs.filter(category=category.upper())  # Category is saved in uppercase

    # Filter by username if provided
    if username:
        blogs = blogs.filter(user__username=username)

    context = {
        'blogs': blogs,
    }
    return render(request, 'keshav_list.html', context)




