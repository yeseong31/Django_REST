from django.urls import path

from todo import views
from todo.views import TodosAPIView, TodoAPIView, DoneTodosAPIView, DoneTodoAPIView

app_name = 'todo'

urlpatterns = [
    # 전체 목록 조회
    # path('', views.todo_list, name='todo_list'),
    # 상세 조회
    # path('<int:pk>/', views.todo_detail, name='todo_detail'),
    # 생성
    # path('post/', views.todo_post, name='todo_post'),
    # 수정
    # path('<int:pk>/edit/', views.todo_edit, name='todo_edit'),
    # 완료 목록 조회
    # path('done/', views.done_list, name='done_list'),
    # 완료
    # path('done/<int:pk>/', views.todo_done, name='todo_done'),

    # ----- APIView -----
    # 전체 목록 조회 & 생성
    path('', TodosAPIView.as_view(), name='todos'),
    # 상세 조회 & 수정
    path('<int:pk>/', TodoAPIView.as_view(), name='todo'),
    # 완료 목록 조회
    path('done/', DoneTodosAPIView.as_view(), name='dones'),
    # 완료
    path('done/<int:pk>/', DoneTodoAPIView.as_view(), name='done'),

]
