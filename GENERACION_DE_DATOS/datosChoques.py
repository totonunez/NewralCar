from faker import Faker
from time import time 
from random import choice, random
import csv

lst =[]
with open('ListaDeDatos.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         lst.append(row['Ciudades'])

fake = Faker()
tiempo = time()
print("CHOQUES")
print("insert into choques (id_evento, ciudad,calle, numeración) values")

while (x<10):
    print("({},'{}','{}','{}'),
    ".format(x,fake.name(),fake.address(), fake.email(),fake.url()))
    x = x+1
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)


