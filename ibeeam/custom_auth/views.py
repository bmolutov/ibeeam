from rest_framework import viewsets

from custom_auth.serializers import UserSerializer
from custom_auth.models import User
from rest_framework.permissions import AllowAny


class RegisterViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
