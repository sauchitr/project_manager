# Generated by Django 4.2 on 2023-04-29 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0006_alter_project_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="deadline",
            field=models.DateField(
                verbose_name=datetime.datetime(
                    2023, 4, 29, 18, 57, 39, 154618, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
