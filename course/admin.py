from django.contrib import admin

from .models import (
    Category, Course,
    CourseSection, CourseReview, Lesson
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'id')
    search_fields = ('name', )


# @admin.register(CourseCategory)
# class CourseCategoryAdmin(admin.ModelAdmin):
#     list_display = ('category_id', 'id')
#     search_fields = ('category_id', )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'short_description', 'price', 'discount_price', 'is_published', 'created_at', 'updated_at', 'id')
    search_fields = ('title', 'price')


@admin.register(CourseSection)
class CourseSectionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_id', 'id')
    search_fields = ('title', )


@admin.register(Lesson)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_id', 'video_url', 'duration', 'is_preview', 'id')
    search_fields = ('title', )


@admin.register(CourseReview)
class CourseReviewsAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'user_id', 'rating', 'created_at', 'id')
    search_fields = ('rating', )