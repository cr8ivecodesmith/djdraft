from django.db import models
from django.contrib.auth.models import User

from .managers import UserProfileManager


class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=False, null=False)
    description = models.CharField(max_length=160, blank=True, null=True, default=None)
    avatar = models.ImageField(null=True, default=None)

    objects = UserProfileManager()

    def __unicode__(self):
        return u'{}'.format(self.user.username)


#### SIGNALS SECTION (KEEP AT BOTTOM)
import signals
#### END SIGNALS SECTION
