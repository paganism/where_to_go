from django.db import models
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField(
        max_length=100,
        db_index=True
    )
    description_short = models.TextField(blank=True)
    description_long = HTMLField(blank=True, null=True)
    coordinates = models.JSONField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlacesImages(models.Model):
    place = models.ForeignKey(
        Places,
        on_delete=models.CASCADE,
        related_name='images_places'
    )
    imgs = models.ImageField(verbose_name='Картинка')
    position = models.IntegerField(
        verbose_name='Позиция',
        blank=True,
        null=True,
        db_index=True,
        default=1
        )

    def __str__(self):
        return f'{self.id} {self.place}'

    @property
    def get_absolute_image_url(self):
        return f'{self.imgs.url}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ('position', )
