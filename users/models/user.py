from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

from django.db.models import (
    TextChoices, CharField, EmailField, TextField, ImageField,
    Model, ForeignKey, CASCADE, BooleanField, TimeField
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        username = email.split('@')[0]

        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    class Role(TextChoices):
        ADMIN = 'admin', 'Admin'
        TEACHER = 'teacher', 'Teacher'
        STUDENT = 'student', 'Student'

    username = CharField(max_length=50, unique=True)
    email = EmailField(max_length=100, unique=True)
    role = CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    full_name = CharField(max_length=100, blank=True)
    avatar = ImageField(upload_to='images/users/', blank=True, null=True)
    bio = TextField(blank=True)
    phone_number = CharField(max_length=20, unique=True, blank=True, null=True)

    is_verify = BooleanField(default=False)
    
    objects = CustomUserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class UserProgress(Model):
    user = ForeignKey(User, CASCADE, related_name="progress")
    lesson = ForeignKey("course.Lesson", CASCADE, related_name="user_progress")
    is_completed = BooleanField(default=False)
    last_accessed = TimeField(auto_now=True)
    completed_at = TimeField(auto_now=True)
