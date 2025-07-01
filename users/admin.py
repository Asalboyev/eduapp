from django.contrib import admin
from users.models import User, UserProgress, TeacherProjects, TeacherProfiles

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'is_verify')
    search_fields = ('username', 'email')


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'lesson_id', 'is_completed', 'completed_at', 'last_accessed')
    search_fields = ('user_id__email', 'lesson_id__title')



@admin.register(TeacherProjects)
class TeacherProjectsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'title')
    search_fields = ('user_id__email', 'title')


@admin.register(TeacherProfiles)
class TeacherProfilesAdmin(admin.ModelAdmin):
    list_display = ('user_id', )