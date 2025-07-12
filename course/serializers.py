from rest_framework import serializers
from .models import Category, Course, CourseSection, Lesson


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['slug', 'created_by']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user.id
        return super().create(validated_data)

class CourseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSection
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

