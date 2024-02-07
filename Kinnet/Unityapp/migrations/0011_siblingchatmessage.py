# Generated by Django 4.2.7 on 2024-02-02 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        # "Unityapp", "0011_siblingchatmessage"  # この行を削除
    ]

    operations = [
        migrations.AddField(
            model_name="diaryentry",
            name="user",
            field=models.ForeignKey(
                default=1,  # ここを適切なユーザーの ID に変更
                on_delete=models.CASCADE,
                to=settings.AUTH_USER_MODEL,
                null=True,
            ),
            preserve_default=False,
        ),
    ]