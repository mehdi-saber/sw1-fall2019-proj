from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *
from django.urls import path

app_name = 'account'

urlpatterns = [
    # Sign up
    path('register/', api_register_user, name="user_register"),
    path('register/verify/', api_register_student_verification, name="student_verification"),
    path('register/verification/refresh_code/', api_refresh_student_verification_code, name="verification_refresh"),


    # Sign in
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),


    # Reset password
    path('reset/', api_reset_password, name="reset_password"),
    path('apply-password/', api_apply_password, name="reset_password"),

    # Edit account
    path('edit/', edit_account, name="edit"),

    path('info/', get_user_tweets, name="get_user_tweets"),

]


