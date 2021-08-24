from django.contrib import admin
from .models import Places

class PlacesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Places, PlacesAdmin)
