from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message,Blog
from .forms import Tweetfromtext,Tweetform, SignUpForm, BlogForm
from django.contrib.auth import login




# this is import for connection or making the logic of buttons and pages...

def tweet_list(request):
    tweets = Message.objects.all().order_by('-created_at')
    return render (request,'tweet/tweet_list.html',{'tweet': tweets})




# this is the user of decorators to guest user.
@login_required
def tweet_create(request):
    if request.method == 'POST':
        tweet_form = Tweetform(request.POST, request.FILES)
        if tweet_form.is_valid():
            tweet = tweet_form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')

    else:
        tweet_form = Tweetform()
        return render (request, 'tweet/tweet_edit.html',{'tweet_form':tweet_form})
    

@login_required    
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Message,pk=tweet_id, user= request.user)
    if request.method == 'POST':
        tweet_form = Tweetfromtext(request.POST, request.FILES,instance=tweet)
        tweet = tweet_form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        return redirect('tweet_list')
        
    else:
        tweet_form = Tweetfromtext(instance=tweet) # this is resposible for show the previous text form model.
    return render (request,'tweet/tweet_edit.html',{'tweet_form': tweet_form})
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Message,pk=tweet_id, user = request.user)
    if request.method == 'POST':
        # not valid for required
        tweet.delete()
        return redirect('tweet_list')
    return render (request,'tweet/tweet_delete.html',{'tweet': tweet})

def SignUp_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form = SignUpForm()
    return render(request,'registration/register.html', {'form': form})


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render (request,'tweet/blog_list.html',{'blog': blogs})

@login_required
def blog_create(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('tweet_list')

    else:
        blog_form = BlogForm()
        return render (request, 'tweet/blog_create.html',{'blog_form':blog_form})
    
@login_required    
def blog_edit(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id, user= request.user)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES,instance=blog)
        blog = blog_form.save(commit=False)
        blog.user = request.user
        blog.save()
        return redirect('tweet_list')
        
    else:
        blog_form = BlogForm(instance=blog) # this is resposible for show the previous text form model.
    return render (request,'tweet/blog_edit.html',{'blog_form': blog_form})