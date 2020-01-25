from rest_framework import serializers

from account.api.methods import send_mail_thread
from account.models import *


class VerificationCodeSerializer(serializers.ModelSerializer):
    verification_code = serializers.SerializerMethodField('get_verification_code')
    expiry_date = serializers.SerializerMethodField('get_expiry_date')

    class Meta:
        model = StudentVerificationCode
        fields = [
            'username',
            'verification_code',
            'expiry_date',
        ]

    @staticmethod
    def get_verification_code():
        generate_pass = ''.join([random.choice(string.ascii_uppercase +
                                string.ascii_lowercase +
                                string.digits)
                                for _ in range(6)]
                                )
        return generate_pass

    @staticmethod
    def get_expiry_date():
        return datetime.now() + timedelta(seconds=600)

    def run(self):
        code = StudentVerificationCode(
            username=self.validated_data['username'],
            verification_code=self.get_verification_code(),
            expiry_date=self.get_expiry_date(),
        )
        code.save()
        email = User.objects.get(username=code.username).email
        try:
            send_mail_thread('HodHod Verification Code', code.verification_code, 'koohsarun.aut@gmail.com', [email, ])
        except Exception as e:
            print(e)
            pass


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'type',
            'email',
            'first_name',
            'last_name',
            'bio',
            'username',
            'password',
            'university',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        student = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            bio=self.validated_data['bio'],
            type=self.validated_data['type'],
            university=self.validated_data['university'],
        )
        student.set_password(self.validated_data['password'])
        student.save()
        return student


class NonStudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'type',
            'email',
            'first_name',
            'last_name',
            'bio',
            'username',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            bio=self.validated_data['bio'],
            type=self.validated_data['type'],
            verified=True,
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_user_name')
    registerDate = serializers.SerializerMethodField('get_register_date')

    class Meta:
        model = User
        fields = [
            "username",
            "name",
            "registerDate",
            "bio",
        ]

    @staticmethod
    def get_user_name(user):
        return f"{user.first_name} {user.last_name}"

    @staticmethod
    def get_register_date(user):
        return f"{user.register_date.year}-{user.register_date.month}-{user.register_date.day}"

