from django.contrib import admin
from .models import *

# Register your models here.


class UserDisplay(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'university')


class UniversityDisplay(admin.ModelAdmin):
    list_display = ('name', 'email_domain')


admin.site.register(User, UserDisplay)
admin.site.register(University, UniversityDisplay)
admin.site.register(StudentVerificationCode)




