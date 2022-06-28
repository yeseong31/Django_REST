from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.models import Profile
from posts.models import Post
from posts.permissions import CustomReadOnly
from posts.serializers import PostSerializer, PostCreateSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [CustomReadOnly]

    # 필터링 적용
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'likes']

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return PostSerializer
        return PostCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  # 회원가입한 User라면 모두 진입 가능
def like_post(request, pk):
    """좋아요 기능: GET"""
    post = get_object_or_404(Post, pk=pk)

    # 자신의 게시글에는 좋아요를 누를 수 없음
    if request.user == post.author:
        return Response({'status': status.HTTP_403_FORBIDDEN,
                         'message': '본인의 게시글에는 좋아요를 누를 수 없습니다.'})
    # 이미 좋아요를 누른 사람이라면... 좋아요 취소
    elif request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return Response({'status': 'ok'})
