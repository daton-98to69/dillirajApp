# Generated by Django 4.2.2 on 2023-07-14 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_customuser_role_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="school_unique_id",
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
