from django.contrib import admin

from .models import InnovoUser, Category, InnovoTag, CpvCode

admin.site.register(InnovoUser)
admin.site.register(Category)
admin.site.register(InnovoTag)
admin.site.register(CpvCode)