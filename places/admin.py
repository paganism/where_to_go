from django.contrib import admin
from .models import Places, PlacesImages


class ImagesInline(admin.TabularInline):
    model = PlacesImages


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]


@admin.register(PlacesImages)
class PlacesImagesAdmin(admin.ModelAdmin):
    pass
