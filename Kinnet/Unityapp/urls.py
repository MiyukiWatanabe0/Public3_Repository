from django.urls import path
from .views import HomePageView, SignupView, LoginView, LogoutView, HomeHomeView
from .views import register_view
from .views import login_view
from .views import logout_view
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('home_home/', HomeHomeView.as_view(), name='home_home'), 
]