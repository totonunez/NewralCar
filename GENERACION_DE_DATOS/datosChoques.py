from faker import Faker
from time import time 
from random import choice, random
import csv

Ciudades = ["Gran_Santiago","Gran Concepcion","Gran Valparaíso","Gran La Serena","Antofagasta",	"Gran Temuco",	"Gran Rancagua","Gran Iquique"," Talca","Arica","Gran Puerto Montt","Gran Chillán",	"Los Ángeles","Calama","Copiapó","Osorno","Gran Quillota","Valdivia","Punta Arenas","Gran San Antonio","Curicó","Ovalle","Linares","Los Andes","Melipilla","San Felipe"]

with open('ListaDeDatos.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         ciudad.append(row['Ciudades'])



fake = Faker()
tiempo = time()
print("CHOQUES")
print("insert into choques (id_evento, ciudad,calle, numeración) values")

while (x<10):
    ciudad = choice(Ciudades)
    print("({},'{}','{}','{}'),".format(x,ciudad,choice(), fake.email())
    x = x+1
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)


