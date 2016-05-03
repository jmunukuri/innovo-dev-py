from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class InnovoUser(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user


class Publication(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    bibtex = models.TextField()
    
    def __unicode__(self):
        return self.title


class Document(models.Model):
    pass

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class InnovoTag(models.Model):
    tag = models.CharField(max_length=255)

    def __unicode__(self):
        return self.tag


class CpvCode(models.Model):
    cpv_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name




