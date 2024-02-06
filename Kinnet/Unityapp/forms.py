from django import forms
from .models import BulletinPost
from .models import DiaryEntry
from django import forms
from .models import Comment
from .models import FamilyChatMessage
from .models import SiblingChatMessage

class BulletinPostForm(forms.ModelForm):
    class Meta:
        model = BulletinPost
        fields = ['region', 'title', 'content']

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['content']

class CommentForm(forms.ModelForm):
     class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'コメントを入力してください'}),
        }

class FamilyChatMessageForm(forms.ModelForm):
    class Meta:
        model = FamilyChatMessage
        fields = ['content']  # 'content' フィールド以外にも必要なフィールドがあれば追加してください

class SiblingChatMessageForm(forms.ModelForm):
    class Meta:
        model = SiblingChatMessage
        fields = ['user', 'content']