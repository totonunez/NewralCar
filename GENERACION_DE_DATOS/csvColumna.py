import csv
lst =[]
with open('Ciudades.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    print(type(reader))
    for row in reader:
        print(row)
