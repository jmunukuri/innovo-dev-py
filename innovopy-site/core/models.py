from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class InnovoUser(models.Model):
	user = models.ForeignKey(User, related_name="innovouser")

