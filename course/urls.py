from django.urls import path
from .views import CategoryListView, CategoryCreateView

urlpatterns = [
    path('category-list/', CategoryListView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
]