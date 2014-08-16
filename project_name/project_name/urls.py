from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import HomepageView

urlpatterns = patterns(
    '',

    # Authentication URLs
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    # Admin URL
    url(r'^admin/', include(admin.site.urls)),

    # Local app URLs
    url(r'^$', HomepageView.as_view(), name='home'),

)
