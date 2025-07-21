from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema
from django.db.models import Q, F
from django.shortcuts import get_object_or_404
from .models import Category, Course, CourseSection, Lesson
from payment.models import Enrollments
from users.models import User
from .serializers import (
    CategorySerializer, CourseSerializer, CourseSectionSerializer,
    LessonSerializer
)
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


# @extend_schema(tags=['course(course)'])
# class CourseListView(generics.ListAPIView):
#     # queryset = Course.objects.filter(is_published=True)
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer


@extend_schema(tags=['course(course)'])
class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.request.user.is_authenticated:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        user = self.request.user

        # bu kurslarni hamma kura oladi login qilgan yoki qilmagan va tekin kurslar
        if not user.is_authenticated:
            return Course.objects.filter(
                is_published=True,
                price__in=[None, 0]
            )

        
        # faqat superuser yoki adminlar ko'radi bularni
        if user.is_superuser or user.role == User.Role.ADMIN:
            return Course.objects.all()

        # kiyinchalik har bir ustoz o'zi yaratgan kurslarni kuradi
        if user.role == User.Role.TEACHER:
            return Course.objects.filter(created_by=user.id)

        # student to'liq to'lagan va is_published kurslarni kuradi, tekin kurslarni ham
        enrolled_course_ids = Enrollments.objects.filter(
            user=user,
            payment_status=Enrollments.PaymentStatus.COMPLETED,
        ).values_list('course_id', flat=True)

        return Course.objects.filter(
            Q(id__in=enrolled_course_ids) |
            Q(is_published=True, price__in=[None, 0])
        ).distinct()



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


# @extend_schema(tags=['course(course section)'])
# class CourseListSectionView(generics.ListAPIView):
#     queryset = CourseSection.objects.all()
#     serializer_class = CourseSectionSerializer


@extend_schema(tags=['course(course section)'])
class CourseListSectionView(generics.ListAPIView):
    serializer_class = CourseSectionSerializer

    def get_queryset(self):
        course_slug = self.kwargs.get("slug")
        course = get_object_or_404(Course, slug=course_slug, is_published=True)
        return CourseSection.objects.filter(course=course).order_by("order_index")


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


# @extend_schema(tags=['course(lesson)'])
# class LessonListView(generics.ListAPIView):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer

#     def get_queryset(self):
#         return Lesson.objects.filter(is_free=True).order_by("order_index")


@extend_schema(tags=['course(lesson)'])
class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        section_id = self.kwargs.get("section_id")

        if not section_id:
            return Lesson.objects.none()

        try:
            section = CourseSection.objects.select_related("course").get(id=section_id)
        except CourseSection.DoesNotExist:
            return Lesson.objects.none()

        course = section.course


        has_paid = Enrollments.objects.filter(
            user=user,
            course=course,
            payment_status=Enrollments.PaymentStatus.COMPLETED
        ).exists()

        if has_paid:
            return Lesson.objects.filter(section=section).order_by("order_index")
        else:
            return Lesson.objects.filter(section=section, is_free=True).order_by("order_index")



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