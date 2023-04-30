# Generated by Django 4.2 on 2023-04-30 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0017_alter_progress_date_alter_project_deadline"),
    ]

    operations = [
        migrations.RemoveField(model_name="task", name="estimated",),
        migrations.AlterField(
            model_name="project",
            name="deadline",
            field=models.DateField(
                verbose_name=datetime.datetime(
                    2023, 4, 30, 10, 42, 23, 686545, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.DeleteModel(name="Progress",),
    ]