from django import forms
from .models import DiaryEntry
from django import forms
from .models import Comment


class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['content']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']