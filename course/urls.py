from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('category-list/', CategoryListView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),
]