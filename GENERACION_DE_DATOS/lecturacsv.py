import csv
 
results = []
with open('ListaDeDatos.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row['ListaDeSensores'])
    print results