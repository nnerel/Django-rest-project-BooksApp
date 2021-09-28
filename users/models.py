from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings 
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser status requires is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser status required is_superuser=True')

        return self.create_user(email, username, first_name, password, **other_fields)


    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError('email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
        

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=120, unique=True)
    first_name = models.CharField(max_length=120, blank=True)
    about = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return """
                    email: %s
                    user name: %s
                    first name: %s
            """     % (self.email, self.username, self.first_name)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        print("Token created")
    if not created:
        print("Token error. Token error Fatal. Token not created")