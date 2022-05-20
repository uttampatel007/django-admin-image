from django.contrib import admin
from django.utils.html import format_html

from myapp.models import DemoModel



class DemoModelCustomAdmin(admin.ModelAdmin):
    list_display = ("title", "image1") 

    def image1(slef, obj):
        return format_html('<img src="{0}" width="auto" height="150px">'.format(obj.image.url))


admin.site.register(DemoModel, DemoModelCustomAdmin)

# github : uttampatel007
# https://github.com/uttampatel007/django-admin-image
# Media root or Media Url
# Urls.py stactic setting
# Pillow 
# Custom Admin Class