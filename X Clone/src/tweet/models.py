from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='tweet_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # set the time when the tweet was created 
    updated_at = models.DateTimeField(auto_now=True) # set the time when the tweet was updated 

    def __str_(self):
        return f'{self.user.username} - {self.text[:10]}'

