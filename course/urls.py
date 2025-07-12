from django.urls import path
from .views import (
    CategoryListView, CategoryCreateView, CategoryUpdateView,
    CategoryDeleteView, CourseCreateView, CourseListView
)

urlpatterns = [
    path('category-list/', CategoryListView.as_view(), name='category-list'),
    path('category-create/', CategoryCreateView.as_view(), name='category-create'),
    path('category-update/<slug:slug>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category-delete/<slug:slug>/', CategoryDeleteView.as_view(), name='category-delete'),
    
    path('courses-create/', CourseCreateView.as_view(), name='courses-create'),
    path('courses-list/', CourseListView.as_view(), name='courses-create'),
]