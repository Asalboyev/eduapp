from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema

from .models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminUserByType


@extend_schema(tags=['course'])
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=['course'])
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserByType]

@extend_schema(tags=['course'])
class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserByType]
    lookup_field = 'id'

@extend_schema(tags=['course'])
class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserByType]
    lookup_field = 'id'
