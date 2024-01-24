# Generated by Django 4.2.7 on 2024-01-23 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Unityapp", "0004_diaryentry_created_at_comment"),
    ]

    operations = [
        migrations.AddField(
          model_name="comment",
          name="user",
          field=models.ForeignKey(
              on_delete=django.db.models.deletion.CASCADE,
              to=settings.AUTH_USER_MODEL,
          ),
          preserve_default=False,
        ),
        migrations.AlterField(
            model_name="comment",
            name="diary_entry",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="Unityapp.diaryentry",
            ),
        ),
    ]
