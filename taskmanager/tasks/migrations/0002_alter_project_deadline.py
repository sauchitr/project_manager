# Generated by Django 4.2 on 2023-04-29 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="deadline",
            field=models.DateField(
                verbose_name=datetime.datetime(
                    2023, 4, 29, 18, 53, 22, 576109, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]