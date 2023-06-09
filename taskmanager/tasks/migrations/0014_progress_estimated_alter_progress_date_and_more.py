# Generated by Django 4.2 on 2023-04-30 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0013_alter_progress_date_alter_project_deadline"),
    ]

    operations = [
        migrations.AddField(
            model_name="progress",
            name="estimated",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name="progress",
            name="date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 4, 30, 10, 18, 58, 468965, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="deadline",
            field=models.DateField(
                verbose_name=datetime.datetime(
                    2023, 4, 30, 10, 18, 58, 466231, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
