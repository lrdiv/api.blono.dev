from django.utils import timezone
from rest_framework import serializers

from .models import Invite

class InviteSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    email_address = serializers.EmailField(max_length=200)
    github_username = serializers.CharField(max_length=200, required=False)
    full_name = serializers.CharField(max_length=200)
    approved = serializers.BooleanField(default=False)
    approved_at = serializers.DateTimeField(default=None, required=False, read_only=True)
    requested_at = serializers.DateTimeField(default=None, required=False)
    already_requested = serializers.BooleanField(default=False, required=False, read_only=True)
    slack_activated = serializers.BooleanField(default=False, required=False, read_only=True)

    def create(self, validated_data):
        return Invite.objects.create(**validated_data)

    def update(self, instance, validated_data):
        was_approved = validated_data.get('approved', False)

        if was_approved and not instance.approved:
            instance.approved_at = timezone.now()
            instance.approved = True

        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.email_address = validated_data.get('email_address', instance.email_address)
        instance.github_username = validated_data.get('github_username', instance.github_username)
        instance.save()
        return instance

