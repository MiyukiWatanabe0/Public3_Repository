from django.contrib import admin
from .models import UserProfile
from .models import FamilyChatMessage, SiblingChatMessage, BulletinPost, DiaryEntry, Comment

admin.site.register(UserProfile)

admin.site.register(FamilyChatMessage)
class FamilyChatMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'timestamp']
    search_fields = ['user__username', 'content']

admin.site.register(SiblingChatMessage)
class SiblingChatMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'timestamp']
    search_fields = ['user__username', 'content']

admin.site.register(BulletinPost)
class BulletinPostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'content', 'timestamp']
    search_fields = ['user__username', 'title', 'content']

admin.site.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'content', 'timestamp']
    search_fields = ['user__username', 'title', 'content']

admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'diary_entry', 'content', 'timestamp']
    search_fields = ['user__username', 'diary_entry__title', 'content']
# Register your models here.
