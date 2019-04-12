from django.utils import timezone
from rest_framework import serializers

from .models import Invite

class InviteSerializer(serializers.Serializer):
    email_address = serializers.EmailField(max_length=200)
    github_username = serializers.CharField(max_length=200, required=False)
    full_name = serializers.CharField(max_length=200)    
    approved = serializers.BooleanField(default=False)
    requested_at = serializers.DateTimeField(default=None, required=False)
    already_requested = serializers.BooleanField(default=False, required=False, read_only=True)

    def create(self, validated_data):
        validated_data['requested_at'] = timezone.now()
        return Invite.objects.create(**validated_data)
