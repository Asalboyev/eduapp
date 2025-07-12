from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema

from .models import Category, Course, CourseSection, Lesson
from .serializers import CategorySerializer, CourseSerializer, CourseSectionSerializer, LessonSerializer
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
    lookup_field = 'slug'


@extend_schema(tags=['course(category)'])
class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserByType]
    lookup_field = 'slug'



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

@extend_schema(tags=['course(course)'])
class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUserByType]
    lookup_field = 'slug'

@extend_schema(tags=['course(course)'])
class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUserByType]
    lookup_field = 'slug'

@extend_schema(tags=['course(course section)'])
class CourseCreateSectionView(generics.CreateAPIView):
    queryset = CourseSection.objects.all()
    serializer_class = CourseSectionSerializer
    permission_classes = [IsAdminUserByType]

@extend_schema(tags=['course(course section)'])
class CourseListSectionView(generics.ListAPIView):
    queryset = CourseSection.objects.all()
    serializer_class = CourseSectionSerializer

@extend_schema(tags=['course(course section)'])
class CourseUpdateSectionView(generics.UpdateAPIView):
    queryset = CourseSection.objects.all()
    serializer_class = CourseSectionSerializer
    permission_classes = [IsAdminUserByType]
    lookup_field = 'id'

@extend_schema(tags=['course(course section)'])
class CourseDeleteSectionView(generics.DestroyAPIView):
    queryset = CourseSection.objects.all()
    serializer_class = CourseSectionSerializer
    permission_classes = [IsAdminUserByType]
    lookup_field = 'id'

@extend_schema(tags=['course(lesson)'])
class LessonCreateView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdminUserByType]

@extend_schema(tags=['course(lesson)'])
class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

@extend_schema(tags=['course(lesson)'])
class LessonUpdateView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdminUserByType]
    lookup_field = 'id'

@extend_schema(tags=['course(lesson)'])
class LessonDeleteView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdminUserByType]
    lookup_field = 'id'