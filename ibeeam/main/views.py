from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from main.serializers import UserFeedbackSerializer, AnonFeedbackSerializer
from main.services import send_email


# TODO: take it out to another service
class FeedbackViewSet(viewsets.GenericViewSet):
    def get_serializer_class(self):
        if self.action == 'send_feedback_by_user':
            return UserFeedbackSerializer
        elif self.action == 'send_feedback_by_anon':
            return AnonFeedbackSerializer

    def send_feedback_by_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=self.request.data,
            context={
                'request': request,
                'email': self.request.user.email
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_email(
            email=self.request.user.email
        )
        return Response(status.HTTP_200_OK)

    def send_feedback_by_anon(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=self.request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_email(
            email=serializer.validated_data['email']
        )
        return Response(status.HTTP_200_OK)
