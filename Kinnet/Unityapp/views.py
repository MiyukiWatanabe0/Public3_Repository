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
from .models import BulletinPost
from .forms import BulletinPostForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import ChatMessage
from Unityapp.models import FamilyChatMessage
from django.contrib import messages
from .forms import CommentForm
from .forms import FamilyChatMessageForm
from Unityapp.models import SiblingChatMessage
from .models import SiblingChatMessage
from .forms import SiblingChatMessageForm
from django.http import Http404
from .forms import CustomUserCreationForm

class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')
    
class SignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_home')
        return render(request, 'signup.html', {'form': form})
        
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        nickname = request.POST.get('nickname')  # 'username'の代わりに'nickname'を使用
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        print(f"Nickname: {nickname}, Password: {password}")

        user = authenticate(request, username=nickname, password=password)
        print(f"Authenticated user: {user}")

        if user is not None:
            login(request, user)
            print("Login successful")

            if not remember_me:
                request.session.set_expiry(0)

            return redirect('home_home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    
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
    
class BulletinBoarPagedView(View):
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
    template_name = 'chat_login.html'

    def get(self, request):
        # GETメソッドの処理を実装
        return render(request, self.template_name, {'form': AuthenticationForm()})

    def post(self, request):
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
            error_message = 'Invalid login credentials'
            return HttpResponse(render(request, 'chat_room.html', {'error': error_message}))
             
class ChatRoomView(View):
    template_name = 'chat_room.html'

    def get(self, request):
        if request.user.is_authenticated:
            # ユーザーがログインしている場合は、チャットルームの画面を表示
            return render(request, self.template_name)
        else:
            # ログインしていない場合は、ログインページにリダイレクト
            return redirect('chat_login')
        
class FamilyChatLoginView(View):
    def get(self, request):
        # 家族チャットログインのビューの実装
        return render(request, 'family_chat_login.html')
        
class FamilyChatRoomLoginView(View):
    template_name = 'family_chat_room_login.html'

    def get(self, request):
        chat_messages = FamilyChatMessage.objects.filter(chat_room='family')
        return render(request, self.template_name, {'chat_messages': chat_messages})

    def post(self, request):
        content = request.POST.get('content')
        message_id = request.POST.get('message_id')

        if message_id:
            # メッセージIDがある場合は、メッセージを削除する
            chat_message = get_object_or_404(FamilyChatMessage, id=message_id)
            chat_message.delete_message()
        elif content:
            # コンテンツがある場合は、新しいメッセージを投稿する
            FamilyChatMessage.objects.create(user=request.user, content=content, chat_room='family')

        return redirect('family_chat_room_login')
    
class EditFamilyChatMessageView(View):
    template_name = 'edit_family_chat_message.html'

    def get(self, request, message_id):
        # 編集するメッセージを取得してフォームに初期値として設定
        message = get_object_or_404(FamilyChatMessage, id=message_id)
        form = FamilyChatMessageForm(instance=message)
        return render(request, self.template_name, {'form': form, 'message_id': message_id})

    def post(self, request, message_id):
        # フォームから送信された内容でメッセージを更新
        message = get_object_or_404(FamilyChatMessage, id=message_id)
        form = FamilyChatMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            # メッセージの編集後の処理を追加してください
            return redirect('family_chat_room_login')  # 例: チャットルームにリダイレクト
        else:
            # フォームが無効な場合、再度編集画面を表示
            return render(request, self.template_name, {'form': form, 'message_id': message_id})
        
class DeleteFamilyChatMessageView(View):
    template_name = 'delete_family_chat_message.html'

    def get(self, request, message_id):
        message = get_object_or_404(FamilyChatMessage, id=message_id)
        return render(request, self.template_name, {'message': message})

    def post(self, request, message_id):
        chat_message = get_object_or_404(FamilyChatMessage, id=message_id)
        chat_message.delete_message()
        return redirect('family_chat_room_login')

class SiblingChatLoginView(View):
    def get(self, request):
        # きょうだいチャットログインのビューの実装
        return render(request, 'sibling_chat_login.html')
    
class SiblingChatRoomLoginView(View):
    template_name = 'sibling_chat_room_login.html'

    def get(self, request):
        chat_messages = SiblingChatMessage.objects.filter(chat_room='sibling')
        return render(request, self.template_name, {'chat_messages': chat_messages})

    def post(self, request):
        content = request.POST.get('content')
        message_id = request.POST.get('message_id')

        if message_id:
            # メッセージIDがある場合は、メッセージを削除する
            chat_message = get_object_or_404(SiblingChatMessage, id=message_id)
            chat_message.delete()
        elif content:
            # コンテンツがある場合は、新しいメッセージを投稿する
            SiblingChatMessage.objects.create(user=request.user, content=content, chat_room='sibling')

        return redirect('sibling_chat_room_login')
          
class EditSiblingChatMessageView(View):
    template_name = 'edit_sibling_chat_message.html'

    def get(self, request, message_id):
        # 編集画面の表示ロジックを追加してください
        message = get_object_or_404(SiblingChatMessage, id=message_id)
        form = SiblingChatMessageForm(instance=message)
        return render(request, self.template_name, {'form': form, 'message': message})

    def post(self, request, message_id):
        message = get_object_or_404(SiblingChatMessage, id=message_id)
        form = SiblingChatMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            # メッセージの編集後の処理を追加してください
            return redirect('sibling_chat_room_login')  # 例: チャットルームにリダイレクト
        else:
            return render(request, self.template_name, {'form': form, 'message': message})
        
class DeleteSiblingChatMessageView(View):
    template_name = 'delete_sibling_chat_message.html'

    def get(self, request, message_id):
        message = get_object_or_404(SiblingChatMessage, id=message_id)
        return render(request, self.template_name, {'message': message})

    def post(self, request, message_id):
        chat_message = get_object_or_404(SiblingChatMessage, id=message_id)
        chat_message.delete()  # delete() メソッドを呼び出す
        return redirect('sibling_chat_room_login')
        
class BulletinBoardView(View):
    template_name = 'bulletin_board.html'

    def get(self, request):
        posts = BulletinPost.objects.all()
        return render(request, self.template_name, {'posts': posts, 'form': BulletinPostForm()})

    def post(self, request):
        form = BulletinPostForm(request.POST)
        if form.is_valid():
            form.save()
        posts = BulletinPost.objects.all()
        return render(request, self.template_name, {'posts': posts, 'form': BulletinPostForm()})

class EditBulletinPostView(View):
    template_name = 'edit_bulletin_post.html'

    def get(self, request, post_id):
        post = BulletinPost.objects.get(id=post_id)
        form = BulletinPostForm(instance=post)
        return render(request, self.template_name, {'form': form, 'post': post})

    def post(self, request, post_id):
        post = BulletinPost.objects.get(id=post_id)
        form = BulletinPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('bulletin_board')

class DeleteBulletinPostView(View):
    template_name = 'delete_bulletin_post.html'

    def get(self, request, post_id):
        try:
            post = BulletinPost.objects.get(id=post_id)
        except BulletinPost.DoesNotExist:
            raise Http404("BulletinPost does not exist")
        return render(request, self.template_name, {'post': post})

    def post(self, request, post_id):
        try:
            post = BulletinPost.objects.get(id=post_id)
        except BulletinPost.DoesNotExist:
            raise Http404("BulletinPost does not exist")

        post.delete()
        return redirect('bulletin_board')
    
class DiaryPageView(View):
    def get(self, request, entry_id):
        entry = DiaryEntry.objects.get(id=entry_id)
        return render(request, 'diary.html', {'entry': entry})

    def post(self, request):
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
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

class DeleteDiaryConfirmView(View):
    template_name = 'delete_diary_confirm.html'

    def get(self, request, entry_id):
        entry = get_object_or_404(DiaryEntry, id=entry_id)
        return render(request, self.template_name, {'entry': entry})

    def post(self, request, entry_id):
        entry = get_object_or_404(DiaryEntry, id=entry_id)
        entry.delete()
        return redirect('diary')

class DiaryDetailView(View):
    def get(self, request, entry_id):
        entry = DiaryEntry.objects.get(id=entry_id)
        comments = Comment.objects.filter(diary_entry=entry)
        form = CommentForm()

        return render(request, 'diary_detail_confirm.html', {'entry': entry, 'comments': comments, 'form': form})
    
    def post(self, request, entry_id):
        entry = get_object_or_404(DiaryEntry, id=entry_id)
        comments = Comment.objects.filter(diary_entry=entry)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.diary_entry = entry
            comment.save()
            return redirect('diary_detail', entry_id=entry_id)

        return render(request, 'diary_detail_confirm.html', {'entry': entry, 'comments': comments, 'form': form})

class DiaryDetailConfirmView(View):
    def get(self, request):
        # ビューのロジックを実装する
        pass
    
class EditCommentView(View):
    def get(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentForm(instance=comment)
        return render(request, 'edit_comment.html', {'form': form, 'comment': comment})

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('diary_detail', entry_id=comment.diary_entry.pk)
        else:
            return render(request, 'edit_comment.html', {'form': form, 'comment': comment})
        
class DeleteCommentView(View):
    def get(self, request, entry_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        return render(request, 'delete_comment.html', {'comment': comment, 'entry_id': entry_id})

    def post(self, request, entry_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
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
