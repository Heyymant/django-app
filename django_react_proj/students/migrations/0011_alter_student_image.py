# Generated by Django 4.0.6 on 2022-07-23 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
