from django.contrib import admin
from badges.models import Badge,Location,BadgerUser

# Register your models here.


admin.site.register(Badge)
admin.site.register(Location)
admin.site.register(BadgerUser)
