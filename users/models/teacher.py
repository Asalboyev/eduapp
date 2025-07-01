from django.db.models import IntegerField, Model, CharField, ForeignKey, CASCADE, TimeField, TextField
from django.utils.timezone import now

from users.models import User


class TeacherProfiles(Model):
    user_id =  ForeignKey(User, CASCADE, related_name='teacher_profiles')
    specialization =  CharField(max_length=255)
    experience_years =  IntegerField()
    website_url = CharField(max_length=255)
    social_links = CharField(max_length=255)
    created_at = TimeField(default=now)
    updated_at = TimeField(default=now)


class TeacherProjects(Model):
    user_id = ForeignKey("User", CASCADE, related_name='teacher_projects')
    title = CharField(max_length=255)
    description = TextField()
    project_url = CharField(max_length=255)
    image_url = CharField(max_length=255)
    created_at = TimeField(default=now)
