from django import forms
from .models import BulletinPost
from .models import DiaryEntry
from django import forms
from .models import Comment
from .models import FamilyChatMessage
from .models import SiblingChatMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Eメールアドレス')
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'maxlength': '10'}))

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if password and len(password) < 10:
           raise forms.ValidationError("パスワードは10文字以上で作成してください。")
        return password

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

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
        fields = ['user', 'content']  # 'content' フィールド以外にも必要なフィールドがあれば追加してください

class SiblingChatMessageForm(forms.ModelForm):
    class Meta:
        model = SiblingChatMessage
        fields = ['user', 'content']