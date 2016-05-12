# utils.py
import json
from datetime import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from innovosite.models import Innovosite, SubOrganization, Building
from asset.models import Asset
from core.models import InnovoUser, Category, InnovoTag, CpvCode

"""
item foreign keys: 
ou
site
building
department (suborg)
"""

# HU site
site = Innovosite.objects.get(pk=1)


# SubOrganizations
def migrate_suborgs():
    global site
    f = open("innovonet-migration-2016-05-11/ou.json", "r")
    d = f.read()
    f.close()
    data_ou = json.loads(d)
    for row in data_ou['RECORDS']:
        data_obj = SubOrganization(name=row['name'], url=row['url'])
        data_obj.org_site = site
        data_obj.save()

# Buildings
def migrate_buildings():
    global site
    f = open("innovonet-migration-2016-05-11/building.json", "r")
    d = f.read()
    f.close()
    data_bldng = json.loads(d)

    for row in data_bldng['RECORDS']:
        data_obj = Building(name=row['name'])
        data_obj.building_site = site
        data_obj.save()

# Items (assets)
def migrate_items():
    f = open("innovonet-migration-2016-05-11/item.json", "r")
    d = f.read()
    f.close()
    data_assets = json.loads(d)
    # data = data_assets[100]
    
    for data in data_assets['RECORDS']:
        data_obj = Asset()
        data_obj.title = data['title'] or None

        try:
            data_obj.organization = SubOrganization.objects.get(pk=int(data['ou_id']))
        except Exception as e:
            print e, data['item_id'], data['ou_id']
            data_obj.organization = None
        
        try:
            data_obj.building = Building.objects.get(pk=int(data['building_id']))
        except Exception as e:
            print e, data['item_id'], data['building_id']
            data_obj.building = None

        try:
            data_obj.date_updated = datetime.strptime(data['date_updated'], '%Y-%m-%d %H:%M:%S') 
        except:
            data_obj.date_updated = None
        
        try:
            data_obj.date_of_purchase = datetime.strptime(data['date_of_purchase'], '%Y-%m-%d %H:%M:%S') 
        except:
            data_obj.date_of_purchase = None;

        try:
            data_obj.date_added = datetime.strptime(data['date_added'], '%Y-%m-%d %H:%M:%S') 
        except:
            data_obj.date_added = None
        
        
        try:
            data_obj.image = data['image'] or None
        except Exception as e:
            print e.message, data['item_id'], 'image'
        
        try:
            data_obj.manufacturer_website = data['manufacturer_website'] or None
        except Exception as e:
            print e.message, data['item_id'], 'manufacturer_website'
        
        try:
            data_obj.cost = data['cost'] or None
        except Exception as e:
            print e.message, data['item_id'], 'cost'
    
        try:
            data_obj.keywords = data['keywords'] or None
        except Exception as e:
            print e.message, data['item_id'], 'keywords'

        try:
            data_obj.availability = data['availability'] or None
        except Exception as e:
            print e.message, data['item_id'], 'availability'
        
        try:
            data_obj.organisation = data['organisation'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'organisation'
        
        try:
            data_obj.comments = data['comments'] or None
        except Exception as e:
            print e.message, data['item_id'], 'comments'

        try:
            data_obj.contact_2_email = data['contact_2_email'] or None
        except Exception as e:
            print e.message, data['item_id'], 'contact_2_email'
        
        try:
            data_obj.contact_1_email = data['contact_1_email'] or None
        except Exception as e:
            print e.message, data['item_id'], 'contact_1_email'
        
        try:
            data_obj.short_description = data['short_description'] or None
        except Exception as e:
            print e.message, data['item_id'], 'short_description'
        
        try:
            data_obj.serial_no = data['serial_no'] or None
        except Exception as e:
            print e.message, data['item_id'], 'serial_no'

        try:
            data_obj.visibility = data['visibility'] or None
        except Exception as e:
            print e.message, data['item_id'], 'visibility'
        
        try:
            data_obj.manufacturer = data['manufacturer'] or None
        except Exception as e:
            print e.message, data['item_id'], 'manufacturer'
        
        try:
            data_obj.full_description = data['full_description'] or None
        except Exception as e:
            print e.message, data['item_id'], 'full_description'
        
        try:
            data_obj.contact_1_name = data['contact_1_name'] or None
        except Exception as e:
            print e.message, data['item_id'], 'contact_1_name'
        
        try:
            data_obj.asset_no = data['asset_no'] or None
        except Exception as e:
            print e.message, data['item_id'], 'asset_no'
        
        try:
            data_obj.contact_2_name = data['contact_2_name'] or None        
        except Exception as e:
            print e.message, data['item_id'], 'contact_2_name'
        
        try:
            data_obj.specification = data['specification'] or None        
        except Exception as e:
            print e.message, data['item_id'], 'specification'
        
        try:
            data_obj.quantity = data['quantity'] or None        
        except Exception as e:
            print e.message, data['item_id'], 'quantity'
        
        try:
            data_obj.year_of_manufacture = data['year_of_manufacture'] or None
        except Exception as e:
            print e.message, data['item_id'], 'year_of_manufacture'
        
        try:
            data_obj.room = data['room'] or None
        except Exception as e:
            print e.message, data['item_id'], 'room'
        
        try:
            data_obj.model_name = data['model']
        except Exception as e:
            print type(e).__name__, e.message, data['item_id'], 'model_name'

        data_obj.save()

def migrate_categories():
    f = open("innovonet-migration-2016-05-11/category.json", "r")
    d = f.read()
    f.close()
    data_cats = json.loads(d)

    for row in data_cats['RECORDS']:
        data_obj = Category(name=row['name'])
        data_obj.save()   

def migrate_tags():
    f = open("innovonet-migration-2016-05-11/tag.json", "r")
    d = f.read()
    f.close()
    data_tags = json.loads(d)

    for row in data_tags['RECORDS']:
        data_obj = InnovoTag(tag=row['tag'])
        data_obj.save()

def migrate_cpv_codes():
    f = open("innovonet-migration-2016-05-11/cpv.json", "r")
    d = f.read()
    f.close()
    data_cpvcodes = json.loads(d)

    for row in data_cpvcodes['RECORDS']:
        data_obj = CpvCode(cpv_id=row['cpv_id'], name=row['name'])
        data_obj.save()

def migrate_users():
    assets = Asset.objects.all()
    user_set = set()
    for a in assets:
        if a.contact_1_email:
            try:
                new_user = User(username=a.contact_1_email, email=a.contact_1_email, is_active=False)
                new_user.save()
                innovuser = InnovoUser(user=new_user)
                innovuser.save()
            
            except Exception as e:
                print e

        if a.contact_2_email:
            try:
                new_user = User(username=a.contact_2_email, email=a.contact_2_email, is_active=False)
                new_user.save()
                innovuser = InnovoUser(user=new_user)
                innovuser.save()
            
            except Exception as e:
                print e

def run_migration_procs():
    migrate_suborgs()
    migrate_buildings()
    migrate_items()
    migrate_categories()
    migrate_tags()
    migrate_cpv_codes()
    migrate_users()
    print "done."


data_assets = {}
def debug():
    global data_assets
    f = open("innovo-migrate/item.json", "r")
    d = f.read()
    f.close()
    data_assets = json.loads(d)
    

    
        