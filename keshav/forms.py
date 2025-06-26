from django import forms
from .models import Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
