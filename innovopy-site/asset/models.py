from __future__ import unicode_literals

from collections import OrderedDict

from django.db import models

from innovosite.models import Innovosite, SubOrganization, Building 
from core.models import DocumentFile 


class Asset(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    organization = models.ForeignKey(SubOrganization, null=True, related_name="assets", blank=True)
    building =  models.ForeignKey(Building, null=True, blank=True)
    room = models.CharField(max_length=256, null=True, blank=True)
    model_name = models.CharField(max_length=256, null=True, blank=True)
    manufacturer = models.CharField(max_length=256, null=True, blank=True)
    manufacturer_website = models.CharField(max_length=256, null=True, blank=True)
    short_desc = models.CharField(max_length=256, null=True, blank=True)
    full_desc = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    contact_1_name = models.CharField(max_length=256, null=True, blank=True)
    contact_1_email = models.CharField(max_length=256, null=True, blank=True)
    contact_2_name = models.CharField(max_length=256, null=True, blank=True)
    contact_2_email = models.CharField(max_length=256, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    related_media = models.ManyToManyField(DocumentFile, blank=True)

    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(null=True, blank=True)
    date_of_purchase = models.DateTimeField(null=True, blank=True)
    date_disposed_of = models.DateTimeField(null=True, blank=True)
    date_archived = models.DateTimeField(null=True, blank=True)   
    end_of_life = models.DateTimeField(null=True, blank=True)
    last_calibration_date = models.DateTimeField(null=True, blank=True)
    next_calibration_date = models.DateTimeField(null=True, blank=True) 
    PAT = models.DateTimeField(null=True, blank=True)
    
    acronym = models.CharField(max_length=24, null=True, blank=True)
    archived = models.IntegerField(null=True, blank=True, default=0)
    asset_no = models.CharField(max_length=256, null=True, blank=True)
    availability = models.CharField(max_length=256, null=True, blank=True)
    calibrated = models.CharField(max_length=4, null=True, blank=True)
    copyright_notice = models.CharField(max_length=256, null=True, blank=True)
    cost = models.CharField(max_length=256, null=True, blank=True) 
    embedded_content = models.TextField(null=True, blank=True)
    finance_id = models.CharField(max_length=256, null=True, blank=True)
    future_upgrades = models.TextField(null=True, blank=True)
    is_disposed_of = models.CharField(max_length=5, null=True, blank=True)
    is_parent = models.IntegerField(null=True, blank=True, default=0)
    last_updated_username = models.CharField(max_length=256, null=True, blank=True)
    last_updated_email = models.CharField(max_length=256, null=True, blank=True)
    maintenance = models.CharField(max_length=256, null=True, blank=True)
    portability = models.CharField(max_length=256, null=True, blank=True) 
    quantity = models.IntegerField(default=1)
    quantity_detail = models.CharField(max_length=256, null=True, blank=True)
    replacement_cost = models.CharField(max_length=256, null=True, blank=True) 
    restrictions = models.CharField(max_length=256, null=True, blank=True)
    serial_no = models.CharField(max_length=256, null=True, blank=True)
    specification = models.TextField(null=True, blank=True)
    supplier_id = models.IntegerField( null=True, blank=True)
    technique = models.CharField(max_length=256, null=True, blank=True)
    training_required = models.IntegerField(null=True, blank=True)
    training_provided = models.IntegerField(null=True, blank=True)
    upgrades = models.TextField(null=True, blank=True)
    usergroup = models.CharField(max_length=256, null=True, blank=True)  
    year_of_manufacture = models.IntegerField(null=True, blank=True)


    def get_as_dict_selected(self, fieldlist=None):
        d = OrderedDict()
        if not fieldlist:
            fieldlist = ('title', 'building', 'room', 'short_desc', 'full_desc', 'contact_1_name', 'contact_1_email',)
        for field in fieldlist:
            prop = eval('self.'+field)
            d[field] = prop or ''
        return d            

    def get_as_dict(self):
        d = {}
        for field in [ f.name for f in self._meta.get_fields(include_parents=False)]:
            prop = eval('self.'+field)
            d[field] = prop or ''
        return d

    def get_absolute_url(self):
        return reverse('asset', args=[self.id])

    def __unicode__(self):
        return self.title





""" TODO: Modeling associations"""

#  item -> tag
#  item -> category
#  item -> publications
#  item -> users
#  item -> files

