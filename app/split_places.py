import csv

upvotes = [1, 10, 50, 100, 200, 500, 1000]


for i in range(len(upvotes)-1):
    min = upvotes[i]
    max = upvotes[i+1]
    f = open(f"split_places_{min}-{max}.csv", "w")
    f.write(f"WKT, name, description\n")

    with open('places.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            if count == 0:
                count += 1
                continue
            if min <= int(row[2].strip()) < max:
                f.write(f"{row[0]},{row[1]},{row[2]}\n")

    f.close()
