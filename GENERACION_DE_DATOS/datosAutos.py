from faker import Faker
from time import time
from random import random, choice


fake = Faker()
tiempo = time()
print("AUTOS")
print("insert into choques (id_auto, largo, ancho, alto, peso_neto, peso_max, tipo_combustible, tipo_auto, cant_pasajero, numeroAro) values")

while (x<10):
    peso_neto = random.uniform(2700, 3860)
    print("({},'{}' (mm) ,'{}' (mm),'{}' (mm),'{}' (mm), '{}' (mm),'{}' (mm),'{}' (mm),'{}' pasajeros, '{}' ),".format(x,random.uniform(3500, 5000),random.uniform(1700, 1900), random.uniform(1300, 1800),peso_neto + random.uniform(500, 1000)))
    x = x+1
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)