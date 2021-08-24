from django.db import models
from django.db.models.fields.files import ImageFileDescriptor


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
