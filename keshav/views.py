from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import Tweetfromtext,Tweetform, SignUpForm
from django.contrib.auth import login




# this is import for connection or making the logic of buttons and pages...

def tweet_list(request):
    tweets = Message.objects.all().order_by('-created_at')
    return render (request,'tweet/tweet_list.html',{'tweet': tweets})

# this is the user of decorators to guest user.
@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = Tweetform(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')

    else:
        form = Tweetform()
        return render (request, 'tweet/tweet_edit.html',{'form':form})
    

@login_required    
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Message,pk=tweet_id, user= request.user)
    if request.method == 'POST':
        form = Tweetfromtext(request.POST, request.FILES,instance=tweet)
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        return redirect('tweet_list')
        
    else:
        form = Tweetfromtext(instance=tweet) # this is resposible for show the previous text form model.
    return render (request,'tweet/tweet_edit.html',{'form': form})
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
