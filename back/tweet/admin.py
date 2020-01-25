from django.contrib import admin
from .models import *
# Register your models here.


class TweetDisplay(admin.ModelAdmin):
    list_display = ('tweeter', 'content')


class CommentDisplay(admin.ModelAdmin):
    list_display = ('author', 'tweet', 'content')


admin.site.register(Tweet, TweetDisplay)
admin.site.register(Comment, CommentDisplay)
