import datetime
import random

from rest_framework import serializers
from tweet.models import *


class NewTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = [
            'tweeter',
            'content',
        ]

    def save(self):
        tweet = Tweet(
            tweeter=self.validated_data['tweeter'],
            content=self.validated_data['content'],
        )
        tweet.save()
        return tweet.pk


class NewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'author',
            'tweet',
            'content',
        ]

    def save(self):
        comment = Comment(
            author=self.validated_data['author'],
            tweet=self.validated_data['tweet'],
            content=self.validated_data['content'],
        )
        comment.save()


class FeedSerializer(serializers.ModelSerializer):
    tweetId = serializers.SerializerMethodField('get_tweet_id')
    retweeted_by = serializers.SerializerMethodField('get_retweeter')
    user = serializers.SerializerMethodField('get_tweet_user_info')
    timeToNow = serializers.SerializerMethodField('get_past_time')
    likes = serializers.SerializerMethodField('get_likes_number')
    retweets = serializers.SerializerMethodField('get_retweets_number')
    comments = serializers.SerializerMethodField('get_comments_number')

    class Meta:
        model = Tweet
        fields = [
            "tweetId",
            "retweeted_by",
            "user",
            "timeToNow",
            "content",
            "likes",
            "retweets",
            "comments",
        ]

    @staticmethod
    def get_tweet_id(tweet):
        return tweet.pk

    @staticmethod
    def get_retweeter(tweet):
        try:
            user = tweet.retweeted_by.first()
        except Exception as e:
            return None
        if random.random()>0.8:
            return {
                'username': user.username
            }
        return None


    @staticmethod
    def get_tweet_user_info(tweet):
        return {'username': tweet.tweeter.username, 'name': str(tweet.tweeter)}

    @staticmethod
    def get_past_time(tweet):
        seconds = (datetime.datetime.now(datetime.timezone.utc) - tweet.time).seconds
        if seconds/60 > 59:
            return f"{int(seconds/3600)}h"
        return f"{int(seconds/60)}m"

    @staticmethod
    def get_likes_number(tweet):
        return tweet.likes.count()

    @staticmethod
    def get_retweets_number(tweet):
        return tweet.retweeted_by.count()

    @staticmethod
    def get_comments_number(tweet):
        return tweet.comments.count()


class TweetInfoSerializer(serializers.ModelSerializer):
    tweetId = serializers.SerializerMethodField('get_tweet_id')
    user = serializers.SerializerMethodField('get_tweet_user_info')
    timeToNow = serializers.SerializerMethodField('get_past_time')
    likes = serializers.SerializerMethodField('get_likes_number')
    retweeters = serializers.SerializerMethodField('get_retweeter_ids')
    retweets = serializers.SerializerMethodField('get_retweets_number')
    comments = serializers.SerializerMethodField('get_comments_number')
    commentList = serializers.SerializerMethodField('get_comments_list')

    class Meta:
        model = Tweet
        fields = [
            "tweetId",
            "user",
            "timeToNow",
            "content",
            "likes",
            "retweeters",
            "retweets",
            "comments",
            'commentList',
        ]

    @staticmethod
    def get_tweet_id(tweet):
        return tweet.pk

    @staticmethod
    def get_retweeter_ids(tweet):
        user = tweet.retweeted_by.all()
        result = []
        for i in user:
            result.append(i.username)
        return result

    @staticmethod
    def get_tweet_user_info(tweet):
        return {'username': tweet.tweeter.username, 'name': str(tweet.tweeter)}

    @staticmethod
    def get_past_time(tweet):
        seconds = (datetime.datetime.now(datetime.timezone.utc) - tweet.time).seconds
        if seconds/60 > 59:
            return f"{int(seconds/3600)}h"
        return f"{int(seconds/60)}m"

    @staticmethod
    def get_likes_number(tweet):
        return tweet.likes.count()

    @staticmethod
    def get_retweets_number(tweet):
        return tweet.retweeted_by.count()

    @staticmethod
    def get_comments_number(tweet):
        return tweet.comments.count()

    @staticmethod
    def get_comments_list(tweet):
        comments = tweet.comments.values()
        result = []
        for i in comments:
            c = Comment.objects.get(pk=i['id'])
            result.append(CommentSerializer(c).data)
        return result


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    author = serializers.SerializerMethodField('get_author_info')
    timeToNow = serializers.SerializerMethodField('get_past_time')
    likes = serializers.SerializerMethodField('get_likes_number')

    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'content',
            'timeToNow',
            'likes',
        ]

    @staticmethod
    def get_id(comment):
        return comment.pk

    @staticmethod
    def get_author_info(comment):
        return {'username': comment.author.username, 'name': str(comment.author)}

    @staticmethod
    def get_past_time(comment):
        seconds = (datetime.datetime.now(datetime.timezone.utc) - comment.time).seconds
        if seconds/60 > 59:
            return f"{int(seconds/3600)}h"
        return f"{int(seconds/60)}m"

    @staticmethod
    def get_likes_number(comment):
        return comment.likes.count()
