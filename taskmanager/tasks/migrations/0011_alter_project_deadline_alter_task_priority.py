# Generated by Django 4.2 on 2023-04-29 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0010_alter_project_deadline_alter_task_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="deadline",
            field=models.DateField(
                verbose_name=datetime.datetime(
                    2023, 4, 29, 21, 27, 52, 484361, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[("H", "High"), ("M", "Medium"), ("L", "Low")],
                default="M",
                max_length=10,
            ),
        ),
    ]
