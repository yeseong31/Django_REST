from rest_framework import serializers

from common.serializers import ProfileSerializer
from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'profile', 'post', 'text')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'text')


class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)  # nested serializer
    comments = CommentSerializer(many=True, read_only=True)  # 댓글 Serializer를 포함하여 댓글 추가, 다수의 댓글 포함

    class Meta:
        model = Post
        fields = ('pk', 'profile', 'title', 'body', 'image', 'published_date', 'likes', 'comments')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'image')
