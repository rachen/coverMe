from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    url = models.URLField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)

    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
