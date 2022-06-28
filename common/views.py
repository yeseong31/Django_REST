from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from common.models import Profile
from common.serializers import RegisterSerializer, SigninSerializer, ProfileSerializer


class RegisterView(generics.CreateAPIView):
    """회원가입: POST"""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class SigninView(generics.GenericAPIView):
    """로그인: POST"""
    serializer_class = SigninSerializer

    def post(self, request):
        # Serializer 통과 후 얻어온 토큰을 그대로 응답해 주는 방식
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
