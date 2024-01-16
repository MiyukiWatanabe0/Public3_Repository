from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

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
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

        return render(request, self.template_name, {'form': form})
        
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')

        user = authenticate(request, username=nickname, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

class LogoutView(View):
    def get(self,request):
        request.session.clear()
        return redirect('home')
           
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
        if form.is_vaild():
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
