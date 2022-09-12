import googlemaps
import api_key

gmaps = googlemaps.Client(key=api_key.google_maps_api)


def get_places(name, location="47.618266,-122.314647", radius=25000):
    places_result = gmaps.places(query=name,
                                 location=location,
                                 radius=radius,
                                 )
    return places_result


def process_places(places_result, length=2):
    place_result_length = min(length, len(places_result['results']))
    processed_places = []

    for i in range(place_result_length):
        if 'food' in set(places_result['results'][i]['types']) or 'restaurant' in set(places_result['results'][i]['types']):
            name_encode = places_result['results'][i]['name'].encode("utf-8", "ignore")
            name_decode = name_encode.decode("utf-8")
            processed_places.append({
                'location': places_result['results'][i]['geometry']['location'],
                'name': name_decode,
                'place_id': places_result['results'][i]['place_id']
            })

    return processed_places


print(get_places(name="Pudge Brothers Pizza"))