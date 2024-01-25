from django import forms
from .models import BulletinPost
from .models import DiaryEntry
from django import forms
from .models import Comment


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