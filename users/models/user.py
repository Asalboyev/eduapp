from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db.models import TextChoices, CharField, EmailField, TextField, ImageField


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


class User(AbstractUser, PermissionsMixin):
    class Role(TextChoices):
        ADMIN = 'admin', 'Admin'
        TEACHER = 'teacher', 'Teacher'
        STUDENT = 'student', 'Student'

    username = CharField(max_length=50, unique=True)
    email = EmailField(max_length=100, unique=True)
    role = CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    full_name = CharField(max_length=100, blank=True)
    avatar = ImageField(upload_to='images/users/')
    bio = TextField(blank=True)
    phone_number = CharField(max_length=20, unique=True, blank=True)
    objects = CustomUserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
