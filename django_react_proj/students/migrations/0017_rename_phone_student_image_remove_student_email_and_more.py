# Generated by Django 4.0.6 on 2022-07-23 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_remove_student_image_remove_student_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='phone',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.AddField(
            model_name='student',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
    ]
