from django.urls import path, re_path
from .views import HomePageView, SignupView, LoginView, LogoutView, HomeHomeView
from .views import register_view
from .views import login_view
from .views import logout_view
from django.contrib.auth.views import PasswordResetView
from .views import ChatView
from .views import BulletinBoardView
from .views import DiaryView
from .views import ChatHomeView, CreateChatRoomView, ChatLoginView, ChatHomePageView
from .views import DiaryView, EditDiaryView, DeleteDiaryView
from .views import DiaryPageView
from .views import get_dialog_content
from .views import DiaryDetailView, EditCommentView, DeleteCommentView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('home_home/', HomeHomeView.as_view(), name='home_home'), 
    path('chat/', ChatView.as_view(), name='chat'),
    path('bulletin_board/', BulletinBoardView.as_view(), name='bulletin_board'),
    path('diary/', DiaryView.as_view(), name='diary'),
    path('chat_home/', ChatHomeView.as_view(), name='chat_home'),
    path('create_chat_room/', CreateChatRoomView.as_view(), name='create_chat_room'),
    path('chat_login/', ChatLoginView.as_view(), name='chat_login'),
    path('chat_home_page/', ChatHomePageView.as_view(), name='chat_home_page'),  
    path('diary/edit/<int:entry_id>/', EditDiaryView.as_view(), name='edit_diary'),
    path('diary/delete/<int:entry_id>/', DeleteDiaryView.as_view(), name='delete_diary'),
    path('diary/', DiaryPageView.as_view(), name='diary'),
    path('get_dialog_content/<int:entry_id>/', get_dialog_content, name='get_dialog_content'),
    path('diary/detail/<int:entry_id>/', DiaryDetailView.as_view(), name='diary_detail'),
    path('diary/detail/<int:entry_id>/', DiaryDetailView.as_view(), name='diary_detail'),
    path('diary/detail/<int:entry_id>/post_comment/', DiaryDetailView.as_view(), name='post_comment'),
    path('diary/detail/<int:entry_id>/edit_comment/<int:comment_id>/', EditCommentView.as_view(), name='edit_comment'),
    path('diary/detail/<int:entry_id>/delete_comment/<int:comment_id>/', DeleteCommentView.as_view(), name='delete_comment'),
    ]
    
