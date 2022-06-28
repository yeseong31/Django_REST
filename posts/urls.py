from django.urls import path
from rest_framework import routers

from posts.views import PostViewSet, like_post, CommentViewSet

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls + [
    # '좋아요' 기능
    path('like/<int:pk>/', like_post, name='like_post')
]
