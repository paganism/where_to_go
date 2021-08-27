from django.contrib import admin
from .models import Places, PlacesImages
from django.utils.html import mark_safe, format_html
from django.conf import settings


class ImagesInline(admin.TabularInline):
    model = PlacesImages
    readonly_fields = ['get_preview', ]
    fields = ('imgs', 'get_preview', 'position')

    @staticmethod
    def get_new_dimensions(width, height, height_restriction):

        ratio = width / height

        new_width = int(height_restriction * ratio)
        new_height = height_restriction

        return new_width, new_height

    def get_preview(self, obj):
        prev_width, prev_height = self.get_new_dimensions(
            obj.imgs.width,
            obj.imgs.height,
            settings.IMAGE_PREVIEW_HEIGHT
            )
        return format_html(
            mark_safe(
                '<img src="{url}" width="{width}" height={height} />'.format(
                    url=obj.imgs.url,
                    width=prev_width,
                    height=prev_height,
                    )
                )
            )


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]


@admin.register(PlacesImages)
class PlacesImagesAdmin(admin.ModelAdmin):
    pass
