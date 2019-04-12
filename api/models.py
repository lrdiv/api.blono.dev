from django.db import models

class Invite(models.Model):
    email_address=models.CharField(max_length=200, unique=True)
    full_name=models.CharField(max_length=200)
    github_username=models.CharField(max_length=200, default=None)
    approved=models.BooleanField(default=False)
    requested_at=models.DateTimeField('date approved')

    def __str__(self):
        return self.full_name
