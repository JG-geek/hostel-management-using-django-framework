# Generated by Django 3.0.3 on 2020-03-22 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0003_student_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
        migrations.DeleteModel(
            name='student_details',
        ),
    ]
