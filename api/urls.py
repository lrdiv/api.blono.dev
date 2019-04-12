from django.urls import include, path

from . import views


urlpatterns=[
    path('admin-invites', views.AdminInviteList.as_view()),
    path('admin-invites/<int:pk>', views.AdminInviteDetail.as_view()),
    path('invites', views.InviteList.as_view()),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
