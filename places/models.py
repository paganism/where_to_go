from django.db import models
from django.conf import settings


class Places(models.Model):
    title = models.CharField(
        max_length=100,
        db_index=True
    )
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True, null=True)
    coordinates = models.JSONField()

    def __str__(self):
        return f'{self.title}'


class PlacesImages(models.Model):
    place = models.ForeignKey(
        Places,
        on_delete=models.CASCADE,
        related_name='images_places'
    )
    imgs = models.ImageField()

    def __str__(self):
        return f'{self.id} {self.place}'

    @property
    def get_absolute_image_url(self):
        return f'{settings.MEDIA_ROOT[:-1]}{self.imgs.url}'
