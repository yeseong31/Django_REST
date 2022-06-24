from django.urls import path

from common.views import RegisterView, SigninView

urlpatterns = [
    # ----- 회원가입 -----
    path('signup/', RegisterView.as_view()),
    # ----- 로그인 -----
    path('signin/', SigninView.as_view()),
]