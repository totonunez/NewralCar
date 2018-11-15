import csv
 
results = []
with open('ListaDeDatos.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    print results
    for i in range(0,len(results)):
        print("results[i]['ListaDeSensores']",)