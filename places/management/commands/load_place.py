from django.core.management.base import BaseCommand
from places.models import Places, PlacesImages
import requests
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'loads place to DB from json'

    def add_arguments(self, parser):
        parser.add_argument('url')

    def handle(self, *args, **options):
        try:
            response = requests.get(options['url']).json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        place, created = Places.objects.get_or_create(
            title=response['title'],
            description_short=response['description_short'],
            description_long=response['description_long'],
            coordinates=response['coordinates']
        )

        if created:
            for image_link in enumerate(response['imgs']):
                response_img = requests.get(image_link[1])
                response_img.raise_for_status()

                new_image = PlacesImages(place=place)
                new_image.imgs.save(
                    f'{image_link[0]}',
                    ContentFile(response_img.content),
                    save=True
                    )
