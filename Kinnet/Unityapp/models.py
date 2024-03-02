from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# YourModelクラスでの利用
class YourModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if self.user is None:
            try:
                self.user = User.objects.get(pk=1)
            except User.DoesNotExist:
                pass  # もしユーザーが存在しない場合の処理
        super().save(*args, **kwargs)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Diary(models.Model):
    content = models.TextField()

class BulletinPost(models.Model):
    region = models.CharField(max_length=50) 
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class DiaryEntry(models.Model):
    # id = models.AutoField(primary_key=True)  # この行を削除するかコメントアウトする
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_date(self):
        return self.created_at.strftime('%Y年%m月%d日 %H:%M')

    def get_absolute_url(self):
        return reverse('diary_detail', args=[str(self.pk)])
    
    def get_user_username(self):
        if self.user:
            return self.user.username
        else:
            return "Unknown User"

class Comment(models.Model):
    diary_entry = models.ForeignKey(DiaryEntry, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('diary_detail', args=[str(self.diary_entry.pk)])

    def __str__(self):
        return f'{self.created_at}'

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    chat_room = models.CharField(max_length=1000, default=None)

    def __str__(self):
        return f"{self.user.username}: {self.content}"

class FamilyChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    chat_room = models.CharField(max_length=50)

    def __str__(self):
        if self.user:
            return f"{self.user.username} - {self.content}"
        else:
            return f"None - {self.content}"

    def delete_message(self):
        self.delete()

class SiblingChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    chat_room = models.CharField(max_length=50)

    def __str__(self):
     if self.user:
        return f"{self.user.username} - {self.content}"
     else:
        return f"None - {self.content}"
    
    def delete_message(self):
        if self.user:
            self.user.delete()
        self.delete()