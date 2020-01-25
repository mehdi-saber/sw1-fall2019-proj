from .serializers import *
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
import jwt
from rest_framework.response import Response


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def add_tweet(request):
    payload = jwt.decode(request.auth.token, verify=False)
    user = User.objects.get(pk=payload['user_id'])
    if user.type == "non-student":
        return Response({
            'error': 'Permission Denied'
        })
    if not user.verified:
        return Response({
            'error': 'You are not verified'
        })
    serializer = NewTweetSerializer(data={
        'tweeter': payload['user_id'],
        'content': request.data['content']
    })
    if serializer.is_valid():
        tweet_id = serializer.save()
        data = {
            'tweetId': tweet_id,
            'error': None
        }
    else:
        data = serializer.errors
    return Response(data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def add_comment(request):
    payload = jwt.decode(request.auth.token, verify=False)
    serializer = NewCommentSerializer(data={
        'author': payload['user_id'],
        'tweet': request.data['tweetId'],
        'content': request.data['content']
    })
    if serializer.is_valid():
        serializer.save()
        data = {
            'tweetId': request.data['tweetId'],
            'error': None
        }
    else:
        data = serializer.errors
    return Response(data)


@api_view(['POST', ])
def get_random_feeds(request):
    tweets = Tweet.objects.order_by("-time")[int(request.data["startIndex"]):int(request.data["endIndex"])]
    feeds = []
    for i in tweets:
        serializer = FeedSerializer(i)
        feeds.append(serializer.data)
    return Response({
        'feeds': feeds
    })


@api_view(['POST', ])
def get_tweet_info(request):
    try:
        tweet = Tweet.objects.get(pk=request.data['tweetId'])
    except Tweet.DoesNotExist:
        return Response({
            'error': 'Tweet does not exist'
        })
    serializer = TweetInfoSerializer(tweet)
    return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def like(request):
    payload = jwt.decode(request.auth.token, verify=False)
    user = User.objects.get(pk=payload.get('user_id'))
    if request.data['type'] == 'tweet':
        element = Tweet.objects.get(pk=request.data['Id'])
    else:
        element = Comment.objects.get(pk=request.data['Id'])
    try:
        if request.data['like'] == 'true':
            element.likes.add(user)
        else:
            element.likes.remove(user)
    except Exception as e:
        return Response({'error': "Something went wrong!"})
    return Response({'error': None})


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def retweet(request):
    payload = jwt.decode(request.auth.token, verify=False)
    user = User.objects.get(pk=payload.get('user_id'))
    tweet = Tweet.objects.get(pk=request.data['tweetId'])
    try:
        if request.data['retweet'] == 'true':
            tweet.retweeted_by.add(user)
        else:
            tweet.retweeted_by.remove(user)
    except Exception as e:
        return Response({'error': "Something went wrong!"})
    return Response({'error': None})





