from django.urls import path
from .views import *

app_name = 'tweet'


urlpatterns = [
    path('add_tweet/', add_tweet, name="add-tweet"),
    path('add_comment/', add_comment, name="add-comment"),

    path('feeds/', get_random_feeds, name='get_feeds'),
    path('get_tweet/', get_tweet_info, name="get_tweet_info"),


    # Reactions
    path('like/', like, name='like-and-dislike'),
    path('retweet/', retweet, name='retweet')
]
