import jwt
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
import threading

from account.models import User


def get_tokens(user):
    user_pk = User.objects.get(username=user.username).pk
    refresh = RefreshToken.for_user(user)
    access_token = jwt.decode(str(refresh.access_token), verify=False)
    access_token['user_id'] = user_pk
    refresh = jwt.decode(str(refresh), verify=False)
    refresh['user_id'] = user_pk
    return jwt.encode(access_token, 'secret'), jwt.encode(refresh, 'secret')


def send_mail_thread(subject, content, origin, to):
    t = threading.Thread(target=send_mail,args=(subject, content, origin, to))
    t.start()
