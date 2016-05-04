from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class DocumentFile(models.Model):
    file = models.FileField(null=True)

    def __unicode__(self):
        return self.file.name

class InnovoUser(models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField(null=True)

    def __unicode__(self):
        return self.user


class Publication(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(null=True)
    bibtex = models.TextField(null=True)
    file = models.FileField(null=True)
    
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




