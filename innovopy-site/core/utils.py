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
    f = open("innovo-migrate/ou.json", "r")
    d = f.read()
    f.close()
    data_ou = json.loads(d)
    for row in data_ou:
        data_obj = SubOrganization(name=row['name'], url=row['url'])
        data_obj.org_site = site
        data_obj.save()

# Buildings
def migrate_buildings():
    f = open("innovo-migrate/building.json", "r")
    d = f.read()
    f.close()
    data_bldng = json.loads(d)

    for row in data_bldng:
        data_obj = Building(name=row['name'])
        data_obj.building_site = site
        data_obj.save()

# Items (assets)
def migrate_items():
    f = open("innovo-migrate/item.json", "r")
    d = f.read()
    f.close()
    data_assets = json.loads(d)
    # data = data_assets[100]
    
    for data in data_assets:
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
            data_obj.next_calibration_date = datetime.strptime(data['next_calibration_date'], '%Y-%m-%d %H:%M:%S')
        except:
            data_obj.next_calibration_date = None
        try:
            data_obj.PAT = datetime.strptime(data['PAT'], '%Y-%m-%d %H:%M:%S')
        except:
            data_obj.PAT = None
        try:
            data_obj.date_updated = datetime.strptime(data['date_updated'], '%Y-%m-%d %H:%M:%S') 
        except:
            data_obj.date_updated = None
        try:
            data_obj.last_calibration_date = datetime.strptime(data['last_calibration_date'], '%Y-%m-%d %H:%M:%S') 
        except:
            data_obj.last_calibration_date = None
        try:
            data_obj.date_disposed_of = datetime.strptime(data['date_disposed_of'], '%Y-%m-%d %H:%M:%S') 
        except:
            data_obj.date_disposed_of = None
        try:
            data_obj.end_of_life = datetime.strptime(data['end_of_life'], '%Y-%m-%d %H:%M:%S') 
        except:
            data_obj.end_of_life = None
        try:
            data_obj.date_of_purchase = datetime.strptime(data['date_of_purchase'], '%Y-%m-%d %H:%M:%S') 
        except:
            data_obj.date_of_purchase = None;
        try:
            data_obj.date_added = datetime.strptime(data['date_added'], '%Y-%m-%d %H:%M:%S') 
        except:
            data_obj.date_added = None
        try:
            data_obj.date_archived = datetime.strptime(data['date_archived'], '%Y-%m-%d %H:%M:%S')
        except:
            data_obj.date_archived = None

        try:
            data_obj.replacement_cost = data['replacement_cost'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'replacement_cost'
        try:
            data_obj.is_parent = data['is_parent'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'is_parent'
        try:
            data_obj.image = data['image'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'image'
        try:
            data_obj.upgrades = data['upgrades'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'upgrades'
        try:
            data_obj.manufacturer_website = data['manufacturer_website'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'manufacturer_website'
        try:
            data_obj.cost = data['cost'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'cost'
        try:
            data_obj.is_disposed_of = data['is_disposed_of'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'is_disposed_of'
        try:
            data_obj.usergroup = data['usergroup'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'usergroup'
        try:
            data_obj.keywords = data['keywords'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'keywords'
        try:
            data_obj.training_required = data['training_required'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'training_required'
        try:
            data_obj.availability = data['availability'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'availability'
        try:
            data_obj.archived = data['archived'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'archived'
        try:
            data_obj.supplier_id = data['supplier_id'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'supplier_id'
        try:
            data_obj.last_updated_username = data['last_updated_username'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'last_updated_username'
        try:
            data_obj.organisation = data['organisation'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'organisation'
        try:
            data_obj.technique = data['technique'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'technique'
        try:
            data_obj.comments = data['comments'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'comments'
        try:
            data_obj.contact_2_email = data['contact_2_email'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'contact_2_email'
        try:
            data_obj.finance_id = data['finance_id'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'finance_id'
        try:
            data_obj.contact_1_email = data['contact_1_email'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'contact_1_email'
        try:
            data_obj.maintenance = data['maintenance'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'maintenance'
        try:
            data_obj.short_description = data['short_description'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'short_description'
        try:
            data_obj.serial_no = data['serial_no'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'serial_no'
        try:
            data_obj.restrictions = data['restrictions'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'restrictions'
        try:
            data_obj.acronym = data['acronym'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'acronym'
        try:
            data_obj.quantity_detail = data['quantity_detail'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'quantity_detail'
        try:
            data_obj.visibility = data['visibility'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'visibility'
        try:
            data_obj.future_upgrades = data['future_upgrades'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'future_upgrades'
        try:
            data_obj.training_provided = data['training_provided'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'training_provided'
        try:
            data_obj.manufacturer = data['manufacturer'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'manufacturer'
        try:
            data_obj.full_description = data['full_description'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'full_description'
        try:
            data_obj.copyright_notice = data['copyright_notice'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'copyright_notice'
        try:
            data_obj.contact_1_name = data['contact_1_name'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'contact_1_name'
        try:
            data_obj.asset_no = data['asset_no'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'asset_no'
        try:
            data_obj.calibrated = data['calibrated'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'calibrated'
        try:
            data_obj.contact_2_name = data['contact_2_name'] or None        
            
        except Exception as e:
            print e.message, data['item_id'], 'contact_2_name'
        try:
            data_obj.embedded_content = data['embedded_content'] or None        
            
        except Exception as e:
            print e.message, data['item_id'], 'embedded_content'
        try:
            data_obj.last_updated_email = str(data['last_updated_email']) or None        
            
        except Exception as e:
            print e.message, data['item_id'], 'last_updated_email'
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
            data_obj.portability = data['portability'] or None
            
        except Exception as e:
            print e.message, data['item_id'], 'portability'
        
        try:
            data_obj.model_name = data['model']
            
        except Exception as e:
            print type(e).__name__, e.message, data['item_id'], 'model_name'

        data_obj.save()

def migrate_categories():
    f = open("innovo-migrate/category.json", "r")
    d = f.read()
    f.close()
    data_cats = json.loads(d)

    for row in data_cats:
        data_obj = Category(name=row['name'])
        data_obj.save()   

def migrate_tags():
    f = open("innovo-migrate/tag.json", "r")
    d = f.read()
    f.close()
    data_tags = json.loads(d)

    for row in data_tags:
        data_obj = InnovoTag(tag=row['tag'])
        data_obj.save()

def migrate_cpv_codes():
    f = open("innovo-migrate/cpv.json", "r")
    d = f.read()
    f.close()
    data_cpvcodes = json.loads(d)

    for row in data_cpvcodes:
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



data_assets = {}
def debug():
    global data_assets
    f = open("innovo-migrate/item.json", "r")
    d = f.read()
    f.close()
    data_assets = json.loads(d)
    

    
        