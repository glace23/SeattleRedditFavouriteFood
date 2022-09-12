import gmaps_location
import csv


f = open("../outputs/places.csv", "w")
f.write(f"WKT, name, description\n")

with open('../outputs/comments.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        if int(row[1]) > 0:
            places_result = gmaps_location.get_places(name=row[0])
            processed_places = gmaps_location.process_places(places_result=places_result)
            skip_processed = set()
            for place in processed_places:
                if (place['location']['lng'], place['location']['lat']) not in skip_processed:
                    f.write(f"POINT({place['location']['lng']} {place['location']['lat']}), {place['name'].capitalize()}, {row[1]}\n")
                skip_processed.add((place['location']['lng'], place['location']['lat']))

f.close()


