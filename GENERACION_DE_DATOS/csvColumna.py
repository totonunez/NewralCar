import csv
lst =[]
with open('ListaDeDatos.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         lst.append(row['Ciudades'])
    
    print(lst)