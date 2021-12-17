import csv

data = []
with open("dataset_2.csv", "r") as f:
    csv_reader = csv.reader(f)
    
    for row in csv_reader:
        data.append(row)

headers = data[0]

planet_data = data[1:]

#Coverting all Planet names to lower case.

for datapoint in planet_data:
    datapoint[2] = datapoint[2].lower()


#Sorting planet names in alphabetical order.

planet_data.sort(key = lambda planet_data: planet_data[2])
with open("dataset_2_sorted.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
