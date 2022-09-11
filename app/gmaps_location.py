import googlemaps
import api_key

gmaps = googlemaps.Client(key=api_key.google_maps_api)
# location_bias = "circle:50000@47.618266,-122.314647"
location = "47.618266,-122.314647"
radius = 10000

places_result = gmaps.places(query="Queen Cà Phê",
                             location=location,
                             radius=radius,
                             )

print(places_result)

for i in places_result['results']:
    print(i)

# candidate_list = places_result["candidates"]
# place_id = candidate_list[0]["place_id"]
#
# reverse_geocode_result = gmaps.reverse_geocode(latlng=place_id)
#
# print(reverse_geocode_result)
