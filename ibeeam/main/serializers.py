from rest_framework import serializers

from main.models import Feedback


class UserFeedbackSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=1024)

    def create(self, validated_data):
        instance = Feedback.objects.create(
            **validated_data,
            email=self.context['email']
        )
        return instance

    def update(self, instance, validated_data):
        instance.email = self.context['email']
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class AnonFeedbackSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=1024)

    def create(self, validated_data):
        instance = Feedback.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
