from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from .serializers import UserSerializer
from .services import delete_user
from custom_auth.models import User


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer

    def create_user(self, request, *args, **kwargs):
        user = User(
            profile_id=self.request.data['profile_id']
        )
        user.save()
        return Response(user.profile_id, status=status.HTTP_201_CREATED)

    def delete_user(self, request, *args, **kwargs):
        is_deleted = delete_user(self.kwargs['profile_id'])
        if is_deleted:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
