from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema

from .models import Category, Course
from .serializers import CategorySerializer, CourseSerializer
from .permissions import IsAdminUserByType


@extend_schema(tags=['course(category)'])
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=['course(category)'])
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserByType]


@extend_schema(tags=['course(category)'])
class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserByType]
    lookup_field = 'id'


@extend_schema(tags=['course(category)'])
class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserByType]
    lookup_field = 'id'



@extend_schema(tags=['course(course)'])
class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUserByType]


@extend_schema(tags=['course(course)'])
class CourseListView(generics.ListAPIView):
    # queryset = Course.objects.filter(is_published=True)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer