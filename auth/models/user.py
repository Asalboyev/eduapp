from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import CharField, EmailField, TextField


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    username = CharField(max_length=50, unique=True, null=True, blank=True)
    email = EmailField(max_length=100, unique=True)
    password = CharField(max_length=255)
    role = CharField(max_length=20, choices=ROLE_CHOICES)
    full_name = CharField(max_length=255, blank=True)
    avatar_url = CharField(max_length=500, blank=True)
    bio = TextField(blank=True)
    phone_number = CharField(max_length=20, unique=True, blank=True)
    objects = CustomUserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
