from django.db import models

# Create your models here.
from account.models import User


class Tweet(models.Model):
    tweeter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')
    retweeted_by = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.pk}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User)
