from django.http import JsonResponse
from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from ..models import Invite
from ..serializers import InviteSerializer


class InviteList(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        invite = Invite.objects.filter(
            email_address=request.data['email_address']).first()

        if invite:
            invite.already_requested = True
            serializer = InviteSerializer(invite)
            return JsonResponse(serializer.data, safe=False)

        serializer = InviteSerializer(data=request.data)

        if serializer.is_valid() and serializer.save():
            return JsonResponse(serializer.data, safe=False)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
