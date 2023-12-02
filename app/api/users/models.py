from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.exceptions import FieldError
from django.utils import timezone
from django.db import models


class CustomManager(BaseUserManager):
    def create_user(self, email, password, *args, **kwargs):
        kwargs.setdefault('is_superuser', False)
        kwargs.setdefault('is_staff', False)

        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, *args, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        self.create_user(email, password, *args, **kwargs)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Your email', unique=True)
    first_name = models.CharField(verbose_name='Your first name', null=True, blank=True)
    last_name = models.CharField(verbose_name='Your last name', null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False, editable=False)
    is_superuser = models.BooleanField(default=False, editable=False)
    objects = CustomManager()

    REQUIRED_FIELDS = ['password', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
