from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from ..models import Invite
from ..serializers import InviteSerializer


class AdminInviteList(APIView):
    def get(self, request, format=None):
        approved = request.query_params.get('approved', 'false') == 'true'
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
