from django.urls import path
from .views import HomePageView, SignupView, LoginView, LogoutView, HomeHomeView
from .views import register_view
from .views import login_view
from .views import logout_view
from django.contrib.auth.views import PasswordResetView
from .views import ChatView
from .views import BulletinBoardView
from .views import DiaryView
from .views import ChatHomeView, CreateChatRoomView, ChatLoginView, ChatHomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('home_home/', HomeHomeView.as_view(), name='home_home'), 
    path('chat/', ChatView.as_view(), name='chat'),
    path('bulletin_board/', BulletinBoardView.as_view(), name='bulletin_board'),
    path('Diary/', DiaryView.as_view(), name='diary'),
    path('chat_home/', ChatHomeView.as_view(), name='chat_home'),
    path('create_chat_room/', CreateChatRoomView.as_view(), name='create_chat_room'),
    path('chat_login/', ChatLoginView.as_view(), name='chat_login'),
    path('chat_home_page/', ChatHomePageView.as_view(), name='chat_home_page'),  
]