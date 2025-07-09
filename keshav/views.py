from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message,Keshav
from .forms import Tweetfromtext,Tweetform, SignUpForm,KeshavForm
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import UserProfile
from django.contrib.auth.models import User




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
    print("Vlog Delete called.")
    tweet = get_object_or_404(Message,pk=tweet_id, user = request.user)
    if request.method == 'POST':
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


    
@login_required
def profile_view(request):
    return render(request, 'registration/profile.html', {
        'user': request.user,
    })

# password change 
@login_required
def custom_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep user logged in
            messages.success(request, 'Your password was changed successfully!')
            return redirect('change')  # your custom success page
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'registration/keshav.html', {'form': form})


# this is for the user profilephoto and profile update
@login_required
def done(request):
    return render(request,'registration/done.html')

@login_required
def profile_view(request):
    return render(request,'registration/profile.html')

@login_required
def profile_edit(request):
    # This line ensures no error happens if userprofile is missing
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user_profile')  # reload profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    return render(request, 'registration/edit_profile.html', {
        'u_form': u_form,
        'p_form': p_form
  
    })


# keshav blog one..
def keshav_list(request):
    blogs = Keshav.objects.all().order_by('-created_at')
    return render(request, 'keshav/keshav_list.html', {'blogs': blogs})


# View a single blog
def keshav_detail(request, pk):
    blog = get_object_or_404(Keshav, pk=pk)
    return render(request, 'keshav/keshav_detail.html', {'blog': blog})

# Create new blog
@login_required
def keshav_create(request):
    if request.method == 'POST':
        form = KeshavForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.user = request.user
            new_blog.save()
            messages.success(request, "Blog created successfully!")
            return redirect('keshav_list')
    else:
        form = KeshavForm()
    return render(request, 'new/keshav_create.html', {'form': form})

# Update blog
@login_required
def keshav_update(request, pk):
    blog = get_object_or_404(Keshav, pk=pk)
    if request.user != blog.user:
        return redirect('keshav_list')
    
    if request.method == 'POST':
        form = KeshavForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog updated successfully!")
            return redirect('keshav_detail', pk=pk)
    else:
        form = KeshavForm(instance=blog)
    return render(request, 'keshav/keshav_form.html', {'form': form})

@login_required    
def keshav_edit(request,pk):
    print("BLOG EDIT CALLED")
    blog = get_object_or_404(Keshav,pk=pk, user= request.user)
    if request.method == 'POST':
        form = KeshavForm(request.POST, request.FILES,instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('keshav_list')
        else:
            print(f"keshav. {form.errors}")        

    return render (request,'new/keshav_edit.html',{'form': form})

# Delete blog
@login_required
def keshav_delete(request, pk):
    print("Keshav Blog is delete")
    blog = get_object_or_404(Keshav, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('keshav_list')
    return render(request,'new/keshav_delete.html',{'blog':blog})