from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=100,
        db_index=True,
        null=True,
        blank=True,
        verbose_name='Интересные места'
    )
    short_description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Краткое описание'
        )
    long_description = HTMLField(
        blank=True,
        null=True,
        verbose_name='Полное описание'
        )
    coordinates = models.JSONField(verbose_name='Координаты')

    def __str__(self): return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='place_images',
        verbose_name='Места'
    )
    img = models.ImageField(verbose_name='Картинка')
    position = models.IntegerField(
        verbose_name='Позиция',
        blank=True,
        null=True,
        db_index=True,
        )

    def __str__(self):
        return f'{self.id} {self.place}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ('position', )
