import csv

dataset1 = []
dataset2 = []

with open("dataset_1.csv", "r") as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        dataset1.append(i)

with open("dataset_2_sorted.csv", "r") as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        dataset2.append(i)

headers1 = dataset1[0]
headers2 = dataset2[0]

planet_data1 = dataset1[1:]
planet_data2 = dataset2[1:]

headers = headers1 + headers2

planet_data = []

for index, datarow in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])

with open("final.csv", "a+")as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)

