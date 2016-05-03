from __future__ import unicode_literals

from collections import OrderedDict

from django.db import models

from innovosite.models import Innovosite, SubOrganization, Building  


class Asset(models.Model):
    title = models.CharField(max_length=256, null=True)
    manufacturer = models.CharField(max_length=256, null=True)
    model_name = models.CharField(max_length=256, null=True)
    short_desc = models.CharField(max_length=256, null=True)
    full_desc = models.TextField(null=True)
    
    organization = models.ForeignKey(SubOrganization, null=True, related_name="assets")
    building =  models.ForeignKey(Building, null=True)

    date_added = models.DateTimeField(null=True)
    date_updated = models.DateTimeField(null=True)
    PAT = models.DateTimeField(null=True)
    last_calibration_date = models.DateTimeField(null=True)
    next_calibration_date = models.DateTimeField(null=True) 
    date_of_purchase = models.DateTimeField(null=True)
    date_disposed_of = models.DateTimeField(null=True)
    end_of_life = models.DateTimeField(null=True)
    date_archived = models.DateTimeField(null=True)

    room = models.CharField(max_length=256, null=True)
    specification = models.TextField(null=True)
    upgrades = models.TextField(null=True)
    future_upgrades = models.TextField(null=True)
    acronym = models.CharField(max_length=24, null=True)
    keywords = models.TextField(null=True)
    technique = models.CharField(max_length=256, null=True)
    availability = models.CharField(max_length=256, null=True)
    restrictions = models.CharField(max_length=256, null=True)
    usergroup = models.CharField(max_length=256, null=True)
    
    portability = models.CharField(max_length=256, null=True) 
    
    image = models.CharField(max_length=256, null=True)
    contact_1_name = models.CharField(max_length=256, null=True)
    contact_1_email = models.CharField(max_length=256, null=True)
    contact_2_name = models.CharField(max_length=256, null=True)
    contact_2_email = models.CharField(max_length=256, null=True)
    manufacturer_website = models.CharField(max_length=256, null=True)
    copyright_notice = models.CharField(max_length=256, null=True)
    last_updated_username = models.CharField(max_length=256, null=True)
    last_updated_email = models.CharField(max_length=256, null=True)
    training_required = models.IntegerField(null=True)
    training_provided = models.IntegerField(null=True)
    quantity = models.IntegerField(default=1)
    quantity_detail = models.CharField(max_length=256, null=True)
    calibrated = models.CharField(max_length=4, null=True)
    asset_no = models.CharField(max_length=256, null=True)
    finance_id = models.CharField(max_length=256, null=True)
    serial_no = models.CharField(max_length=256, null=True)
    year_of_manufacture = models.IntegerField(null=True)
    supplier_id = models.IntegerField( null=True)
    cost = models.CharField(max_length=256, null=True) 
    replacement_cost = models.CharField(max_length=256, null=True) 
    maintenance = models.CharField(max_length=256, null=True)
    is_disposed_of = models.CharField(max_length=5, null=True)
    comments = models.TextField(null=True)
    archived = models.IntegerField(null=True, default=0)
    is_parent = models.IntegerField(null=True, default=0)
    embedded_content = models.TextField(null=True)

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

