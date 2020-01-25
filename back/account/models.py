import random
import string

from django.db import models
from django.contrib.auth.models import AbstractUser
from account.methods import *
from datetime import timedelta, datetime, timezone


# Create your models here.


class User(AbstractUser):
    # first name, last name and email is built-in
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=30)
    pic = models.FileField(upload_to=pic_path, null=True, default='default/profile.png')
    followings = models.ManyToManyField('self', blank=True, related_name='followings')
    followers = models.ManyToManyField('self', blank=True, related_name='followers')
    bio = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)
    university = models.ForeignKey('University', null=True, on_delete=models.CASCADE, related_name="students")
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class University(models.Model):
    name = models.CharField(max_length=50)
    email_domain = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name}"


class StudentVerificationCode(models.Model):
    username = models.CharField(max_length=50)
    verification_code = models.CharField(max_length=10)
    expiry_date = models.DateTimeField()

    @property
    def is_expired(self):
        if datetime.now(timezone.utc) > self.expiry_date:
            return True
        return False

    @staticmethod
    def get_verification_code():
        generate_pass = ''.join([random.choice(string.ascii_uppercase +
                                string.ascii_lowercase +
                                string.digits)
                                for _ in range(6)]
                                )
        return generate_pass

    def update_expiry_date(self, value=600):
        self.expiry_date += timedelta(seconds=value)

