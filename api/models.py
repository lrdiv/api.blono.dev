from django.db import models
from django.utils import timezone


class Invite(models.Model):
    email_address = models.CharField(max_length=200, unique=True)
    full_name = models.CharField(max_length=200)
    github_username = models.CharField(max_length=200, default=None)
    approved = models.BooleanField(default=False)
    requested_at = models.DateTimeField('date requested', default=timezone.now)
    approved_at = models.DateTimeField('date approved', null=True, blank=True, default=None)
    slack_activated = models.BooleanField(default=False)

    def __str__(self):
        return self.email_address
