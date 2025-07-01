import uuid
from django.db.models import (Model, CharField, TextField, TimeField,ForeignKey, CASCADE, DecimalField,
    BooleanField, IntegerField, SlugField)
from django.utils.timezone import now
from django.utils.text import slugify



class Categories(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True, max_length=255, editable=False)
    description = TextField()
    created_at = TimeField(default=now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if Categories.objects.filter(slug=self.slug).exists():
            self.slug += uuid.uuid4().__str__().split('-')[-1]
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

class CourseCategories(Model):
    name = CharField(max_length=255)
    category_id = ForeignKey(Categories, CASCADE, related_name="course_category")

    def __str__(self):
        return self.name


class Course(Model):
    title = CharField(max_length=255)
    course_category_id = ForeignKey(CourseCategories, CASCADE, related_name="course")
    slug = SlugField(unique=True, max_length=255, editable=False)
    description = TextField()
    short_description = CharField(max_length=255)
    price = DecimalField(decimal_places=2, max_digits=10)
    discount_price = DecimalField(decimal_places=2, max_digits=10)
    thumbnail_url = CharField(max_length=255)
    is_published = BooleanField(default=False)
    created_by = TimeField()
    created_at = TimeField(default=now)
    updated_at = TimeField(default=now)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if Course.objects.filter(slug=self.slug).exists():
            self.slug += uuid.uuid4().__str__().split('-')[-1]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CourseSections(Model):
    course_id = ForeignKey(Course, CASCADE, related_name="course_sections")
    title = CharField(max_length=255)
    order_index = IntegerField()


class Lessons(Model):
    section_id = ForeignKey(CourseSections, CASCADE, related_name="lessons")
    title = CharField(max_length=255)
    content = TextField()
    video_url = CharField(max_length=255)
    duration = IntegerField()
    order_index = IntegerField()
    is_preview = BooleanField(default=False)


class CourseReviews(Model):
    course_id = ForeignKey(Course, CASCADE, related_name="course_reviews")
    user_id = ForeignKey("users.User", CASCADE, related_name="course_reviews")
    rating = IntegerField()
    comment = TextField()
    created_at = TimeField(default=now)
