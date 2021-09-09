from django.shortcuts import render
from places.models import Place
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.urls import reverse


def index(request):

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in Place.objects.all():

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    place.coordinates['lng'],
                    place.coordinates['lat']]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place_detail', args={place.id})
            }
        }

        geo_json['features'].append(feature)

    context = {'geo_json': geo_json}

    return render(request, 'index.html', context)


def get_place_by_id(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related('place_images'),
        id=place_id
        )
    place_images_urls = [
        i.img.url for i in place.place_images.all().order_by('position')
        ]

    pl = {
        'title': place.title,
        'imgs': place_images_urls,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': place.coordinates
        }

    return JsonResponse(
        pl,
        safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 4}
        )
