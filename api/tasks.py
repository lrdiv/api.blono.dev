from __future__ import absolute_import, unicode_literals
import os

from celery import shared_task
from slackclient import SlackClient
from blono_dev_server import settings
from .models import Invite

@shared_task
def send_slack_invite(invite_pk):
    invite = Invite.objects.get(pk=invite_pk)
    token = os.environ.get('SLACK_API_TOKEN')
    client = SlackClient(token)

    res = client.api_call('users.admin.invite', email=invite.email_address)
    if res['ok']:
        invite.slack_activated = True
        invite.save()

    return res
