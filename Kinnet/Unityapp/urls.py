from django.urls import path, re_path
from .views import HomePageView, SignupView, LoginView, LogoutView, HomeHomeView
from .views import register_view
from .views import login_view
from .views import logout_view
from django.contrib.auth.views import PasswordResetView
from .views import ChatView
from .views import ChatRoomView 
from .views import ChatLoginView
from .views import BulletinBoardView
from .views import EditBulletinPostView, DeleteBulletinPostView
from .views import DiaryView
from .views import ChatHomeView, CreateChatRoomView, ChatLoginView, ChatRoomView
from .views import get_dialog_content
from .views import DiaryDetailView, EditCommentView, DeleteCommentView
from .views import EditDiaryView, DeleteDiaryView,DiaryPageView
from .views import FamilyChatLoginView, SiblingChatLoginView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('home_home/', HomeHomeView.as_view(), name='home_home'), 
    path('chat/', ChatView.as_view(), name='chat'), 
    path('chat_login/', ChatLoginView.as_view(), name='chat_login'),
    path('bulletin_board/', BulletinBoardView.as_view(), name='bulletin_board'),
    path('bulletin_board/edit/<int:post_id>/', EditBulletinPostView.as_view(), name='edit_bulletin_post'),
    path('bulletin_board/delete/<int:post_id>/', DeleteBulletinPostView.as_view(), name='delete_bulletin_post'),
    path('diary/', DiaryView.as_view(), name='diary'),
    path('chat_home/', ChatHomeView.as_view(), name='chat_home'),
    path('create_chat_room/', CreateChatRoomView.as_view(), name='create_chat_room'),
    path('family_chat_login/', FamilyChatLoginView.as_view(), name='family_chat_login'),
    path('sibling_chat_login/', SiblingChatLoginView.as_view(), name='sibling_chat_login'),
    path('chat_room/', ChatRoomView.as_view(), name='chat_room'),
    path('diary/edit/<int:entry_id>/', EditDiaryView.as_view(), name='edit_diary'),
    path('diary/delete/<int:entry_id>/', DeleteDiaryView.as_view(), name='delete_diary'),
    path('diary/', DiaryPageView.as_view(), name='diary'),
    path('get_dialog_content/<int:entry_id>/', get_dialog_content, name='get_dialog_content'),
    path('diary/detail/<int:entry_id>/', DiaryDetailView.as_view(), name='diary_detail'),
    path('diary/detail/<int:entry_id>/edit_comment/<int:comment_id>/', EditCommentView.as_view(), name='edit_comment'),
    path('diary/detail/<int:entry_id>/delete_comment/<int:comment_id>/', DeleteCommentView.as_view(), name='delete_comment'),
    path('diary/detail/<int:entry_id>/post_comment/', DiaryDetailView.as_view(), name='post_comment'),
    path('chat_room/', ChatRoomView.as_view(), name='chat_room'),
] 

    
