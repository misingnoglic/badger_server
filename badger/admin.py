from django.contrib import admin
from badger.models import Badge,Location,BadgerUser,Category

# Register your models here.


admin.site.register(Badge)
admin.site.register(Location)
admin.site.register(BadgerUser)
admin.site.register(Category)