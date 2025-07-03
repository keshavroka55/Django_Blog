from django.db import models
# this is added for the timezone....
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator


# this is the tweet one .
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(validators=[MaxLengthValidator(240)])
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:10]}"
# this is the first one of blog with some limitations.
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
    
# this is for the profile photo
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', default='default.jpg')
    blank = True,
    null = True

    def __str__(self):
        return self.user.username
    
# improve version of blog 
class Keshav(models.Model):
    class BlogCategory(models.TextChoices):
        PERSONAL = 'PERSONAL', 'Personal'
        TRAVEL = 'TRAVEL', 'Travel'
        FOOD = 'FOOD', 'Food'
        STORYTIME = 'STORYTIME', 'Storytime'
        LEARNING = 'LEARNING', 'Learning'
        PROJECT = 'PROJECT', 'Project'
        CHALLENGE = 'CHALLENGE', 'Challenge'
        OTHER = 'OTHER', 'Other'
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    photo = models.ImageField(upload_to='blogphotos/', blank=True, null=True)
    category = models.TextChoices
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=300)
    content = models.TextField()
    summary = models.TextField(max_length=500)

    category = models.CharField(
        max_length=20,
        choices=BlogCategory.choices,
        default=BlogCategory.OTHER
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.title[:50]}"
    
# the messages one.
class Chat(models.Model):
    sender = models.ForeignKey(User, related_name=('send_messages'), on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name=('received_messages'), on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default= False)

    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.content[:20]}"



