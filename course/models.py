from django.db import models
from django.db.models import Model, CharField, TextField, TimeField, ForeignKey, CASCADE, DecimalField, BooleanField, \
    IntegerField
from django.utils.timezone import now



class Categories(Model):
  name = CharField(max_length=255)
  slug = CharField(max_length=255)
  description = TextField()
  created_at = TimeField(default=now)

class CourseCategories(Model):
    name = CharField(max_length=255)
    category_id = ForeignKey("Categories", CASCADE, related_name="course_category")

class Course(Model):
    title = CharField(max_length=255)
    course_category_id = ForeignKey("CourseCategories", CASCADE, related_name="course")
    slug = CharField(max_length=255)
    description = TextField()
    short_description = CharField(max_length=255)
    price = DecimalField(decimal_places=2, max_digits=10)
    discount_price = DecimalField(decimal_places=2, max_digits=10)
    thumbnail_url = CharField(max_length=255)
    is_published = BooleanField(default=False)
    created_by = TimeField()
    created_at = TimeField(default=now)
    updated_at = TimeField(default=now)

class CourseSections(Model):
    course_id = ForeignKey("Course", CASCADE, related_name="course_sections")
    title = CharField(max_length=255)
    order_index = IntegerField()

class Lessons(Model):
    section_id = ForeignKey("CourseSections", CASCADE, related_name="lessons")
    title = CharField(max_length=255)
    content = TextField()
    video_url = CharField(max_length=255)
    duration  = IntegerField()
    order_index = IntegerField()
    is_preview = BooleanField(default=False)

class CourseReviews(Model):
    course_id = ForeignKey("Course", CASCADE, related_name="course_reviews")
    user_id = ForeignKey("User", CASCADE, related_name="course_reviews")
    rating = IntegerField()
    comment = TextField()
    created_at = TimeField(default=now)

