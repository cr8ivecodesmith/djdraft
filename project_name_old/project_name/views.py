from django.shortcuts import render
from django.views.generic import View
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .serializers import UserSerializer


class HomepageView(View):
    template_name = '{{ project_name }}/home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class UserProfileView(View):
    template_name = '{{ project_name }}/profile_view.html'

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')

        # Make sure that the user exists
        try:
            user = User.objects.get(
                username=username,
                is_staff=False,
                is_superuser=False,
                is_active=True
            )
        except User.DoesNotExist:
            raise Http404

        context = {
            'view_user': user,
        }

        return render(request, self.template_name, context)


class UserProfileEditView(View):
    template_name = '{{ project_name }}/profile_edit.html'

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')

        # Check if the person viewing this page is logged in
        if not request.user and request.user.is_anonymous():
            raise Http404

        # Check if the person viewing is viewing his/her own profile
        if username != request.user.username:
            raise Http404

        context = {}

        return render(request, self.template_name, context)


class UserListAPIView(ListAPIView):
    """ List all active public users

        Endpoint: /api/v1/users/list
    """
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.model.objects.filter(
            is_staff=False,
            is_superuser=False,
            is_active=True
        )


class UserDetailsAPIView(RetrieveAPIView):
    """ Get active public user details

        Endpoint: /api/v1/users/details/:username
    """
    model = User
    serializer_class = UserSerializer
    lookup_url_kwarg = 'username'
    lookup_field = 'username'

    def get_queryset(self):
        qs = self.model.objects.filter(
            is_staff=False,
            is_superuser=False,
            is_active=True
        )

        if not qs.exists():
            return Response(status.HTTP_404_NOT_FOUND)

        return qs
