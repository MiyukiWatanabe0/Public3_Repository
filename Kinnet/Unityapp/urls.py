from django.contrib import admin
from django.urls import path, re_path
from .views import HomePageView, SignupView, LoginView,  HomeHomeView
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
from .views import DiaryDetailView, EditCommentView, DeleteCommentView, DeleteDiaryConfirmView
from .views import EditDiaryView, DiaryPageView
from .views import FamilyChatLoginView, SiblingChatLoginView
from .views import FamilyChatRoomLoginView, SiblingChatRoomLoginView
from .views import DiaryDetailView
from .views import EditFamilyChatMessageView, DeleteFamilyChatMessageView
from .views import EditSiblingChatMessageView,  DeleteSiblingChatMessageView
from .views import DeleteBulletinPostView
from .views import DiaryDetailConfirmView
from .views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
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
    path('diary/delete-confirm/<int:entry_id>/', DeleteDiaryConfirmView.as_view(), name='delete_diary_confirm'),
    path('diary/', DiaryPageView.as_view(), name='diary'),
    path('get_dialog_content/<int:entry_id>/', get_dialog_content, name='get_dialog_content'),
    path('diary/detail/<int:entry_id>/', DiaryDetailView.as_view(), name='diary_detail'),
    path('diary/detail/<int:entry_id>/edit_comment/<int:comment_id>/', EditCommentView.as_view(), name='edit_comment'),
    path('chat_room/', ChatRoomView.as_view(), name='chat_room'),
    path('family_chat_room_login/', FamilyChatRoomLoginView.as_view(), name='family_chat_room_login'),
    path('sibling_chat_room_login/', SiblingChatRoomLoginView.as_view(), name='sibling_chat_room_login'),
    path('diary/detail/<int:entry_id>/delete_comment/<int:comment_id>/', DeleteCommentView.as_view(), name='delete_comment'),
    path('family_chat_room_login/', FamilyChatRoomLoginView.as_view(), name='family_chat_room_login'),
    path('edit_family_chat_message/<int:message_id>/', EditFamilyChatMessageView.as_view(), name='edit_family_chat_message'),
    path('delete_family_chat_message/<int:message_id>/', DeleteFamilyChatMessageView.as_view(), name='delete_family_chat_message'),
    path('edit_sibling_chat_message/<int:message_id>/', EditSiblingChatMessageView.as_view(), name='edit_sibling_chat_message'),
    path('delete_sibling_chat_message/<int:message_id>/', DeleteSiblingChatMessageView.as_view(), name='delete_sibling_chat_message'),
    path('diary/delete-confirm/<int:entry_id>/', DeleteDiaryConfirmView.as_view(), name='delete_diary_confirm'),
    path('bulletin_board/delete/<int:post_id>/', DeleteBulletinPostView.as_view(), name='delete_bulletin_post'),
    path('diary/detail/<int:entry_id>/', DiaryDetailView.as_view(), name='diary_detail'),
    path('edit_comment/<int:comment_id>/', EditCommentView.as_view(), name='edit_comment'),
    path('diary_detail_confirm/', DiaryDetailConfirmView.as_view(), name='diary_detail_confirm'),
    ]