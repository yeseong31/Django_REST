from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

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
