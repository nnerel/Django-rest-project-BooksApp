from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser status requires is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser status required is_superuser=True')

        return self.create_user(email, user_name, first_name, password, **other_fields)


    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError('email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
        

class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=120, unique=True)
    first_name = models.CharField(max_length=120, blank=True)
    about = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']
