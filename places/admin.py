from django.contrib import admin
from .models import Places, PlacesImages


class PlacesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Places, PlacesAdmin)


class PlacesImagesAdmin(admin.ModelAdmin):
    pass


admin.site.register(PlacesImages, PlacesImagesAdmin)
