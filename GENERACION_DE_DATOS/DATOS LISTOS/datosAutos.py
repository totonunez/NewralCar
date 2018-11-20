from faker import Faker
from time import time
from random import random, choice, randint


fake = Faker()
tiempo = time()
combustible = ["gasolina98", "gasolina95", "gasolina93", "Diesel"]
tautos = ["Sedan", "Station Wagon", "Doble Cabina", "Hatchback","SUV", "Furgon"]

print("AUTOS")
print("insert into autos (id_auto, largo, ancho, alto, peso_neto, peso_max, tipo_combustible, tipo_auto, cant_pasajero, numeroAro) values")

for x in range(0,10):
    peso_neto = randint(2700, 3860)
    print("({},'{}[mm]' ,'{}[mm]','{}[mm]','{}[mm]', '{}[mm]','{}','{}','{}' pasajeros, '{}' ),".format(x,randint(3500, 5000),randint(1700, 1900), randint(1300, 1800),peso_neto,peso_neto + randint(500, 1000), choice(combustible), choice(tautos), choice([2,4,6]), choice(['Aro 24','Aro 26','Aro 28']) ))


print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)
