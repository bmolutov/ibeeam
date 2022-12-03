import os

from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from jose import jwt
from django.contrib.auth.models import User

from .serializers import UserSerializer, LoginSerializer
from .services import delete_user
from utils.generators import get_tokens_for_user


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer

    def create_user(self, request, *args, **kwargs):
        user = User.objects.create_user(
            username=self.request.data['username'],
            password=self.request.data['password']
        )
        return Response(user.username, status=status.HTTP_201_CREATED)

    def delete_user(self, request, *args, **kwargs):
        is_deleted = delete_user(self.kwargs['username'])
        if is_deleted:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.GenericViewSet):
    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'login':
            return LoginSerializer

    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.data['aux_token']

        SECRET_KEY = os.getenv('JWT_SECRET_KEY') # noqa
        ALGORITHM = "HS256" # noqa

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get('sub')

        user = User.objects.get(username=username)
        return Response(get_tokens_for_user(user))
