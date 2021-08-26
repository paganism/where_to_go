from django.shortcuts import render
from places.models import Places

def index(request):

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in Places.objects.all():

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.coordinates['lng'], place.coordinates['lat']]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json"
            }
        }

        geo_json['features'].append(feature)

    context = {'geo_json': geo_json}

    return render(request, 'index.html', context)
