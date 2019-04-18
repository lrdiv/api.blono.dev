from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('admin-invites', views.AdminInviteList.as_view()),
    path('admin-invites/<int:primary_key>', views.AdminInviteDetail.as_view()),
    path('admin-auth', obtain_auth_token),
    path('invites', views.InviteList.as_view())
]
