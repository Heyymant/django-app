# Generated by Django 4.0.6 on 2022-07-23 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_remove_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
