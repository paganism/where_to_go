from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import mark_safe, format_html
from django.conf import settings
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ['get_preview', ]
    fields = ('img', 'get_preview', )
    extra = 1

    @staticmethod
    def get_new_dimensions(width, height, height_restriction):

        ratio = width / height

        new_width = int(height_restriction * ratio)
        new_height = height_restriction

        return new_width, new_height

    def get_preview(self, obj):
        prev_width, prev_height = self.get_new_dimensions(
            obj.img.width,
            obj.img.height,
            settings.IMAGE_PREVIEW_HEIGHT
            )
        return format_html(
            '<img src="{}" width="{}" height={} />',
                obj.img.url,
                prev_width,
                prev_height,
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    search_fields = ['title']


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place', )
    autocomplete_fields = ['place', ]
