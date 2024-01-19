from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
import pdb
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
            return render(request, 'login.html')
        
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
        # DiaryViewの実装
        return render(request, 'diary.html')
    
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

# Create your views here.
