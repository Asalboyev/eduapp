from django.contrib import admin

from .models import (
    Categories, CourseCategories, Course,
    CourseSections, CourseReviews, Lessons
)


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'id')
    search_fields = ('name', )


@admin.register(CourseCategories)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_id', 'id')
    search_fields = ('name', )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'short_description', 'price', 'discount_price', 'is_published', 'created_at', 'updated_at', 'id')
    search_fields = ('title', 'price')


@admin.register(CourseSections)
class CourseSectionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_id', 'id')
    search_fields = ('title', )


@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_id', 'video_url', 'duration', 'is_preview', 'id')
    search_fields = ('title', )


@admin.register(CourseReviews)
class CourseReviewsAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'user_id', 'rating', 'created_at', 'id')
    search_fields = ('rating', )