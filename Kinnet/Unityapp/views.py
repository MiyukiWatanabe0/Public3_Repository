from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
import pdb
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import DiaryEntry, Comment
from .forms import DiaryEntryForm, CommentForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')
    
class SignupView(View):
    template_name = 'signup.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        # pdb.set_trace()
        if form.is_valid():
            print("True")
            user = form.save()
            login(request, user)
            return redirect('home')

        print("False")
        return render(request, self.template_name, {'form': form})
        
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # pdb.set_trace()
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")

        user = authenticate(request, username=username, password=password)
        print(f"Authenticated user: {user}")

        # pdb.set_trace()
        if user is not None:
            login(request, user)
            print("Login successful")
            return redirect('home_home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

class LogoutView(View):
    def get(self,request):
        request.session.clear()
        return redirect('home')
    
class HomeHomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            # ログインユーザーが存在する場合
            return render(request, 'home_home.html', {'user': request.user})
        else:
            # ログインしていない場合の処理（例: ログインページへのリダイレクトなど）
            # お好みに合わせて実装してください
            return render(request, 'login')
        
class ChatView(View):
    def get(self, request):
        # ChatViewの実装
        return render(request, 'chat_home.html')
    
class BulletinBoardView(View):
    def get(self, request):
        # BulletinBoardViewの実装
        return render(request, 'bulletin_board.html')

class DiaryView(View):
    def get(self, request):
        entries = DiaryEntry.objects.all()
        return render(request, 'diary.html', {'entries': entries, 'form': DiaryEntryForm()})

    def post(self, request):
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            form.save()
        entries = DiaryEntry.objects.all()
        return render(request, 'diary.html', {'entries': entries, 'form': DiaryEntryForm()})
    
class ChatHomeView(View):
    def get(self, request):
        return render(request, 'chat_home.html')
    
class CreateChatRoomView(View):
    def get(self, request):
        # チャットルーム作成の実装
        return render(request, 'create_chat_room.html')

class ChatLoginView(View):
    def get(self, request):
        # ログインの実装
        return render(request, 'chat_login.html')

class ChatHomePageView(View):
    def get(self, request):
        # チャットホームページの実装
        return render(request, 'chat_home_page.html')
    
class DiaryPageView(View):
    def get(self, request):
        entries = DiaryEntry.objects.all()
        return render(request, 'diary.html', {'entries': entries, 'form': DiaryEntryForm()})

    def post(self, request):
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('diary')

class EditDiaryView(View):
    def get(self, request, entry_id):
        entry = DiaryEntry.objects.get(id=entry_id)
        form = DiaryEntryForm(instance=entry)
        return render(request, 'edit_diary.html', {'form': form, 'entry': entry})

    def post(self, request, entry_id):
        entry = DiaryEntry.objects.get(id=entry_id)
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
        return redirect('diary')

class DeleteDiaryView(View):
    def get(self, request, entry_id):
        entry = DiaryEntry.objects.get(id=entry_id)
        entry.delete()
        return redirect('diary')

class DiaryDetailView(View):
    def get(self, request, entry_id):
        entry = DiaryEntry.objects.get(id=entry_id)
        comments = Comment.objects.filter(diary_entry=entry)
        form = CommentForm()
        return render(request, 'diary_detail.html', {'entry': entry, 'comments': comments, 'form': form})

    def post(self, request, entry_id):
        entry = DiaryEntry.objects.get(id=entry_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.diary_entry = entry
            comment.user = request.user
            comment.save()
        return redirect('diary_detail', entry_id=entry_id)

    def post_comment(self, request, entry_id):
        # Handle the comment submission here, similar to the post method in DiaryDetailView
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                entry = DiaryEntry.objects.get(id=entry_id)
                comment = form.save(commit=False)
                comment.diary_entry = entry
                comment.user = request.user
                comment.save()
        return HttpResponse("Comment submitted successfully")  # You can customize the response as needed

class EditCommentView(View):
    def get(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        form = CommentForm(instance=comment)
        return render(request, 'edit_comment.html', {'form': form, 'comment': comment})

    def post(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return redirect('diary_detail', entry_id=comment.diary_entry.pk)

class DeleteCommentView(View):
    def get(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        entry_id = comment.diary_entry.pk # 追加
        return render(request, 'delete_comment.html', {'comment': comment})

    def post(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        entry_id = comment.diary_entry.pk  # 追加
        comment.delete()
        return redirect('diary_detail', entry_id=entry_id)
    
def signup_view(request):
    return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    # 新規登録処理が完了した後、ログイン画面にリダイレクト
    # ここに新規登録処理のコードを追加
    return redirect('login')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()

        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    # ログアウト処理のコードを追加
    # ここにログアウト処理のコードを追加
    return redirect('home')

def get_dialog_content(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id)
    dialog_content = {'entryId': entry_id, 'content': entry.content}
    return JsonResponse(dialog_content)

# Create your views here.
