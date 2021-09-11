from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage
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

        place_to_save = {
            'short_description': response['description_short'],
            'long_description': response['description_long'],
            'coordinates': response['coordinates']
        }

        place, created = Place.objects.get_or_create(
            title=response['title'],
            defaults=place_to_save
        )

        if not created:
            return

        for image_part_name, image_link in enumerate(response['imgs']):
            response_img = requests.get(image_link)
            response_img.raise_for_status()

            new_image = PlaceImage(place=place)
            new_image.img.save(
                f'{image_part_name}',
                ContentFile(response_img.content),
                save=True
            )
