import uuid
from django.db.models import (
    Model, CharField, TextField, TimeField, ForeignKey,
    CASCADE, DecimalField, BooleanField, IntegerField,
    SlugField, ManyToManyField, Index, DateTimeField)

from django.utils.timezone import now
from django.utils.text import slugify
from django.contrib.auth import get_user_model





class Category(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True, max_length=255, editable=False)
    description = TextField()
    created_at = TimeField(default=now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if Category.objects.filter(slug=self.slug).exists():
            self.slug += uuid.uuid4().__str__().split('-')[-1]
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Course(Model):
    title = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, editable=False)
    description = TextField(blank=True, null=True)
    short_description = CharField(max_length=255, blank=True, null=True)
    price = DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_price = DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    thumbnail_url = CharField(max_length=255, blank=True, null=True)
    is_published = BooleanField(default=False)
    created_by = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    categories = ManyToManyField(Category, related_name='courses')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if Course.objects.filter(slug=self.slug).exists():
            self.slug += uuid.uuid4().__str__().split('-')[-1]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        indexes = [
            Index(fields=['created_by'], name='idx_courses_created_by')
        ]




class CourseSection(Model):
    course = ForeignKey('Course', on_delete=CASCADE, related_name="course_sections")
    title = CharField(max_length=255)
    order_index = IntegerField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Lesson(Model):
    section = ForeignKey(CourseSection, on_delete=CASCADE, related_name="section_lessons")
    title = CharField(max_length=255)
    content = TextField()
    video_url = CharField(max_length=255)
    duration = IntegerField(help_text="Duration in seconds")
    order_index = IntegerField()
    is_preview = BooleanField(default=False)

    def __str__(self):
        return self.title


class CourseReview(Model):
    course = ForeignKey('Course', on_delete=CASCADE, related_name='course_reviews')
    user = ForeignKey(get_user_model(), on_delete=CASCADE, related_name='course_reviews')
    rating = IntegerField()
    comment = TextField()
    created_at = DateTimeField(default=now)

    def __str__(self):
        return f"{self.user} rated {self.course} - {self.rating}⭐"