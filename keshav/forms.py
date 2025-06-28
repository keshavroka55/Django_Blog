from django import forms
from .models import Message,Blog,Keshav
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class Tweetform(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text','photo']

# this is for only edit the text not the photo
class Tweetfromtext(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email Address.')

    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','subtitle','content','summary']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']


class KeshavForm(forms.ModelForm):
    class Meta:
        model = Keshav
        fields = ['title','photo','subtitle','category','content','summary']