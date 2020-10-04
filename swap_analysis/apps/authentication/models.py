from django.db import models
import uuid
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = "email"

    objects = UserManager()
