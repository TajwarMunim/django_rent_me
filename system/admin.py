from django.contrib import admin
from . models import Owners
from . models import Renter
@admin.register(Owners)
class Owner(admin.ModelAdmin):
    list_display=[
        'username','fullname','nid_no','email_id','address'
    ]

@admin.register(Renter)
class Renter(admin.ModelAdmin):
    list_display=[
         'username','fullname','nid_no','email_id','occupation'
    ]