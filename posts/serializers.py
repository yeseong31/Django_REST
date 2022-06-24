from rest_framework import serializers

from common.serializers import ProfileSerializer
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)  # nested serializer

    class Meta:
        model = Post
        fields = ('pk', 'profile', 'title', 'body', 'image', 'published_date', 'likes')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'image')
