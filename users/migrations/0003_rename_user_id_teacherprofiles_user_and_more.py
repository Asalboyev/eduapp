# Generated by Django 5.2.3 on 2025-07-03 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprogress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherprofiles',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='teacherprojects',
            old_name='user_id',
            new_name='user',
        ),
    ]
