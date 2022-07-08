from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField
from .managers import AccountManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=155, unique=True)
    username = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='username')
    image = models.ImageField(upload_to='media/profiles')
    bio = models.TextField(max_length=2000, default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'slug': self.slug})
