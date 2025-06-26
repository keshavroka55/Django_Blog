from django.db import models
# this is added for the timezone....
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(validators=[MaxLengthValidator(240)])
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:10]}"

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=300)
    content = models.TextField()
    summary = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.title[:50]}"

    




