# Generated by Django 4.2.2 on 2023-07-14 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="academic_year",
            name="class_info",
        ),
        migrations.RemoveField(
            model_name="academic_year",
            name="student",
        ),
        migrations.RemoveField(
            model_name="academic_year",
            name="teacher",
        ),
    ]
