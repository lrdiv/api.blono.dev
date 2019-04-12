from django.http import JsonResponse
from django.utils import timezone

from rest_framework import status
from rest_framework.views import APIView

from ..models import Invite
from ..serializers import InviteSerializer


class InviteList(APIView):
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


class AdminInviteList(APIView):
    def get(self, request, format=None):
        approved = False
        if request.query_params.get('approved', None) == 'true':
            approved = True

        invites = Invite.objects.filter(approved=approved)
        serializer = InviteSerializer(invites, many=True)
        return JsonResponse(serializer.data, safe=False)


class AdminInviteDetail(APIView):
    def put(self, request, pk, format=None):
        invite = Invite.objects.get(pk=pk)
        serializer = InviteSerializer(invite, data=request.data)

        if serializer.is_valid() and serializer.save():
            return JsonResponse(serializer.data, safe=False)

        return JsonResponse(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
