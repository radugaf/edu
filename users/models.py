import uuid
from datetime import datetime

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, email: str, password: str = None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email: str = self.normalize_email(email)
        email: str = email.lower()

        user: UserAccount = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_teacher(self, email: str, password: str = None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)

        user.is_teacher = True
        user.save(using=self._db)

        return user

    def create_student(self, email: str, password: str = None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)

        user.is_student = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str = None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, editable=False)
    email: str = models.EmailField("User Email", max_length=255, unique=True)
    first_name: str = models.CharField("First Name", max_length=255)
    last_name: str = models.CharField("Last Name", max_length=255)

    is_active: bool = models.BooleanField("Is Active", default=False)
    is_student: bool = models.BooleanField("Is Student", default=False)
    is_teacher: bool = models.BooleanField("Is Teacher", default=False)

    # Helpers
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    modified_at: datetime = models.DateTimeField(auto_now=True)
    is_staff: bool = models.BooleanField("Is staff", default=False)

    # Other Django necessary fields
    objects = UserAccountManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['email']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self) -> str:
        return self.email
