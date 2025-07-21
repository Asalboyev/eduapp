from django.urls import path
from .views import (
    CategoryListView, CategoryCreateView, CategoryUpdateView,
    CategoryDeleteView, CourseCreateView, CourseListView, CourseUpdateView, CourseDeleteView, CourseCreateSectionView,
    CourseListSectionView, CourseUpdateSectionView, CourseDeleteSectionView, LessonCreateView, LessonListView,
    LessonDeleteView, LessonUpdateView
)

urlpatterns = [
    path('category-list/', CategoryListView.as_view(), name='category-list'),
    path('category-create/', CategoryCreateView.as_view(), name='category-create'),
    # path('category-update/<slug:slug>/', CategoryUpdateView.as_view(), name='category-update'),
    # path('category-delete/<slug:slug>/', CategoryDeleteView.as_view(), name='category-delete'),
    
    path('courses-create/', CourseCreateView.as_view(), name='courses-create'),
    path('courses-list/', CourseListView.as_view(), name='courses-list'),
    # path('course-update/<slug:slug>/', CourseUpdateView.as_view(), name='courses-update'),
    # path('course-delete/<slug:slug>/', CourseDeleteView.as_view(), name='course-delete'),

    path('coursesection-create/', CourseCreateSectionView.as_view(), name='course section-create'),
    # path('coursesection-list/', CourseListSectionView.as_view(), name='course section-list'),
    path("courses/<slug:slug>/sections/", CourseListSectionView.as_view(), name="course-sections-by-slug"),
    # path('coursesection-update/<int:id>/', CourseUpdateSectionView.as_view(), name='course section-update'),
    # path('coursesection-delete/<int:id>/', CourseDeleteSectionView.as_view(), name='course section-delete'),

    path('lesson-create/', LessonCreateView.as_view(), name='lesson-create'),
    # path('lesson-list/', LessonListView.as_view(), name='lesson-list'),
    path('sections/<int:section_id>/lessons/', LessonListView.as_view(), name='lesson-by-section'),

#     path('lesson-update/<int:id>/', LessonUpdateView.as_view(), name='lesson-update' ),
#     path('lesson-delete/<int:id>/', LessonDeleteView.as_view(), name='lesson-delete'),
]