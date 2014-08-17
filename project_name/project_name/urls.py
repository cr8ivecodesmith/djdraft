from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    HomepageView,
    UserProfileView,
    UserProfileEditView,
    UserListAPIView,
    UserDetailsAPIView,
)

api_v1_patterns = format_suffix_patterns(patterns(
    '',
    url(
        r'users/list',
        UserListAPIView.as_view(),
        name='api_v1_users_list',
    ),
    url(
        r'users/details/(?P<username>\w+)',
        UserDetailsAPIView.as_view(),
        name='api_v1_users_details',
    ),
))

urlpatterns = patterns(
    '',

    # Authentication URLs
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    # Admin URL
    url(r'^admin/', include(admin.site.urls)),

    # Local app URLs
    url(r'^$', HomepageView.as_view(), name='home'),
    url(r'^(?P<username>\w+)/$', UserProfileView.as_view(), name='user_profile_view'),
    url(r'^(?P<username>\w+)/edit/$', UserProfileEditView.as_view(), name='user_profile_edit'),
    url(r'^api/v1/', include(api_v1_patterns, namespace='api_v1'))
)
