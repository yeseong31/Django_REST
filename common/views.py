from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from common.serializers import RegisterSerializer, SigninSerializer


class RegisterView(generics.CreateAPIView):
    """회원가입: POST"""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class SigninView(generics.GenericAPIView):
    """로그인: POST"""
    serializer_class = SigninSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data  # validate()의 return 값
        return Response({'token': token.key}, status=status.HTTP_200_OK)
