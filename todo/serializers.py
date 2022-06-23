from rest_framework import serializers

from todo.models import Todo


class TodoSimpleSerializer(serializers.ModelSerializer):
    """
    전체 조회
    """
    class Meta:
        model = Todo
        fields = ('id', 'title', 'complete', 'important')


class TodoDetailSerializer(serializers.ModelSerializer):
    """
    상세 조회
    """
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'created', 'complete', 'important')


class TodoCreateSerializer(serializers.ModelSerializer):
    """
    생성 및 수정
    """
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important')
