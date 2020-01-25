from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from tweet.api.serializers import TweetInfoSerializer
from tweet.models import Tweet
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from account.api.methods import get_tokens, send_mail_thread


# Create your views here.


@api_view(['POST', ])
def api_register_user(request):
    if request.data['type'] == "student":
        university = University.objects.filter(email_domain=request.data['email'].split('@')[1])
        if not university.exists():
            return Response(status.HTTP_404_NOT_FOUND)
        data = {'university': university[0].pk}
        for key, value in request.data.items():
            data[key] = value
        serializer = StudentRegisterSerializer(data=data)
    elif request.data['type'] == "non-student":
        serializer = NonStudentRegisterSerializer(data=request.data)
    else:
        return {
            'error': 'Invalid type',
            'jwtToken': None
        }
    if serializer.is_valid():
        user = serializer.save()
        if serializer.validated_data['type'] == 'student':
            code = VerificationCodeSerializer(data={
                'username': serializer.validated_data['username']
            })
            if code.is_valid():
                code.run()
                access_token, refresh = get_tokens(user)
                data = {
                    'error': None,
                    'jwtToken': {
                        'access': access_token,
                        'refresh': refresh
                    },
                    'message': 'Please check your email for validation'
                }
            else:
                data = code.errors
        else:
            access_token, refresh = get_tokens(user)
            data = {
                'error': None,
                'jwtToken': {
                    'access': access_token,
                    'refresh': refresh,
                },
                'message': None
            }
    else:
        data = serializer.errors
        data['jwtToken'] = None
    return Response(data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def api_register_student_verification(request):
    try:
        if User.objects.get(username=request.data['username']).verified:
            return Response({
                'message': 'You are already verified'
            })
    except User.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    try:
        sys_code = StudentVerificationCode.objects.get(username=request.data['username'])
    except StudentVerificationCode.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if sys_code.is_expired:
        return Response({
            'error': 'Code has expired'
        })
    if sys_code.verification_code == request.data['verificationCode']:
        user = User.objects.get(username=request.data['username'])
        user.verified = True
        user.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'error': None,
            'jwtToken': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            },
            'message': None
        }
        sys_code.delete()
    else:
        data = {
            'error': 'Wrong code'
        }
    return Response(data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def api_refresh_student_verification_code(request):
    try:
        user = User.objects.get(username=request.data['username'])
        if user.verified:
            return Response({
                'message': 'You are already verified'
            })
    except User.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    sys_code = StudentVerificationCode.objects.filter(username=request.data['username']).order_by('-pk')
    if not sys_code.exists():
        return Response(status.HTTP_404_NOT_FOUND)
    sys_code = sys_code[0]
    sys_code.verification_code = sys_code.get_verification_code()
    sys_code.update_expiry_date()
    sys_code.save()
    try:
        email = User.objects.get(username=sys_code.username).email
        send_mail_thread('HodHod Verification Code', sys_code.verification_code, 'koohsarun.aut@gmail.com', [email, ])
    except Exception as e:
        print(e)
        pass
    return Response({
        'error': None
    })


@api_view(['POST', ])
def api_reset_password(request):
    email = request.data['email']
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({
            "message": "This mail is not registered."
        })
    ver_code = StudentVerificationCode(username=user.username,
                                       verification_code=StudentVerificationCode.get_verification_code(),
                                       expiry_date=datetime.now(timezone.utc) + timedelta(seconds=600)
                                       )
    ver_code.save()
    send_mail_thread('HodHod reset password verification code',
                     ver_code.verification_code,
                     'koohsarun.aut@gmail.com', [user.email, ])
    data = {
        "message": "Check your mail for verification code."
    }
    return Response(data)


@api_view(['POST', ])
def api_apply_password(request):
    try:
        user = User.objects.get(email=request.data['email'])
        ver_code = StudentVerificationCode.objects.get(username=user.username)
    except User.DoesNotExist:
        return Response({
            'error': 'This email is not registered'
        })
    except StudentVerificationCode.DoesNotExist:
        return Response({
            'error': 'No request to change password for this email has been issued'
        })
    if ver_code.is_expired:
        data = {
            'error': 'verification code has expired'
        }
    else:
        if request.data['verificationCode'] == ver_code.verification_code:
            user.set_password(request.data['password'])
            user.save()
            data = {
                'error': None
            }
            ver_code.delete()
        else:
            data = {
                'error': 'Wrong verification code'
            }
    return Response(data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def edit_account(request):
    try:
        user = User.objects.get(username=request.data['username'])
    except User.DoesNotExist:
        return Response({
            'error': 'User does not exist'
        })
    for key, value in request.items():
        if key == 'password':
            user.set_password(value)
        elif key == 'bio':
            user.bio = value
    user.save()
    access_token, refresh = get_tokens(user)
    return Response({
        'error': None,
        'jwt': {
            'access_token': access_token,
            'refresh': refresh
        }
    })


@api_view(['POST', ])
def get_user_tweets(request):
    try:
        user = User.objects.get(username=request.data['username'])
    except User.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    data = {'user': UserSerializer(user).data}
    feeds = []
    try:
        for i in user.tweets.values().order_by('-time')[int(request.data['startIndex']):int(request.data['endIndex'])]:
            tweet = Tweet.objects.get(pk=i['id'])
            feeds.append(TweetInfoSerializer(tweet).data)
        data['feeds'] = feeds
        return Response(data)
    except Exception as e:
        return Response(status.HTTP_400_BAD_REQUEST)
