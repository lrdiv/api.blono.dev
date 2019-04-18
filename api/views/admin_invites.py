from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from ..models import Invite
from ..serializers import InviteSerializer
from ..tasks import send_slack_invite


class AdminInviteList(APIView):
    def get(self, request):
        approved = request.query_params.get('approved', 'false') == 'true'
        invites = Invite.objects.filter(approved=approved)
        serializer = InviteSerializer(invites, many=True)
        return JsonResponse(serializer.data, safe=False)


class AdminInviteDetail(APIView):
    def put(self, request, primary_key):
        invite = Invite.objects.get(pk=primary_key)
        serializer = InviteSerializer(invite, data=request.data)

        if not serializer.is_valid() or not serializer.save():
            return JsonResponse(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        send_slack_invite.delay(primary_key)
        return JsonResponse(serializer.data, safe=False)
