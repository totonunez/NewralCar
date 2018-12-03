import csv
lst =[]
with open('Ciudades.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader)
    for row in reader:
        lst.append(row)
    print(lst)
    for x in lst:
        print(x['Arica'])
