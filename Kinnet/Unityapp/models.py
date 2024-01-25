from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

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
    region = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class DiaryEntry(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_date(self):
        return self.created_at.strftime('%Y年%m月%d日 %H:%M')

    def get_absolute_url(self):
        return reverse('diary_detail', args=[str(self.pk)])

class Comment(models.Model):
    diary_entry = models.ForeignKey(DiaryEntry, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('diary_detail', args=[str(self.pk)])

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'
    

# Create your models here.
