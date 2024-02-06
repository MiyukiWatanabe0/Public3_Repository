# Generated by Django 4.2.7 on 2024-02-06 06:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Unityapp", "0011_siblingchatmessage"),
    ]

    operations = [
        migrations.AddField(
            model_name="diaryentry",
            name="user",
            field=models.ForeignKey(
                default=datetime.datetime(
                    2024, 2, 6, 6, 54, 8, 635738, tzinfo=datetime.timezone.utc
                ),
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
