from django.urls import path

from common.views import RegisterView, SigninView, ProfileView

urlpatterns = [
    # ----- 회원가입 -----
    path('signup/', RegisterView.as_view()),
    # ----- 로그인 -----
    path('signin/', SigninView.as_view()),
    # ----- 프로필 -----
    path('profile/<int:pk>/', ProfileView.as_view()),
]