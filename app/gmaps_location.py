import googlemaps
import api_key

gmaps = googlemaps.Client(key=api_key.google_maps_api)
name = "tianfu"
location = "47.618266,-122.314647"
radius = 25000

places_result = gmaps.places(query=name,
                             location=location,
                             radius=radius,
                             )

print(places_result)

place_result_length = min(2, len(places_result['results']))
processed_places = []
print(len(places_result['results']))

for i in range(place_result_length):
    if 'food' in set(places_result['results'][i]['types']) or 'restaurant' in set(places_result['results'][i]['types']):
        name_encode = places_result['results'][i]['name'].encode("utf-8", "ignore")
        name_decode = name_encode.decode("utf-8")
        processed_places.append({
            'location': places_result['results'][i]['geometry']['location'],
            'name': name,
            'place_id': places_result['results'][i]['place_id']
        })

print(processed_places)

f = open("places.csv", "w")
f.write(f"WKT, name, description\n")
for place in processed_places:
    f.write(f"POINT({place['location']['lng']} {place['location']['lat']}), {place['name'].capitalize()}, {10}\n")
f.close()
