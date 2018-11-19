from faker import Faker
from time import time
from random import random, choice


fake = Faker()
x = 0
tiempo = time()
combustible = ["gasolina98", "gasolina95", "gasolina93", "Diesel"]
tautos = ["Sedán", "Station Wagon", "Doble Cabina", "Hatchback","SUV", "Furgón"]
print("AUTOS")
print("insert into autos (id_auto, largo, ancho, alto, peso_neto, peso_max, tipo_combustible, tipo_auto, cant_pasajero, numeroAro) values")

while (x<10):
    peso_neto = random.uniform(2700, 3860)
<<<<<<< HEAD
    print("({},'{}' (mm) ,'{}' (mm),'{}' (mm),'{}' (mm), '{}' (mm),'{}' (mm),'{}' (mm),'{}' pasajeros, '{}' ),".format(x,random.uniform(3500, 5000),random.uniform(1700, 1900), random.uniform(1300, 1800),peso_neto + random.uniform(500, 1000), choice(combustible), choice(tautos), choice([2,4,6]), choice([24,26,28]) ))
=======
    print("('{}','{}' (mm) ,'{}' (mm),'{}' (mm),'{}' (mg), '{}' (mg),'{}','{}','{}' pasajeros, '{}' ),".format(x,random.uniform(3500, 5000),random.uniform(1700, 1900), random.uniform(1300, 1800),peso_neto + random.uniform(500, 1000), choice(combustible), choice(tautos), choice([2,4,6]), choice([24,26,28]) ))
>>>>>>> 1ec94bd8cdaced4a09ee46ee472dd665372bd51a
    x = x+1
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)
