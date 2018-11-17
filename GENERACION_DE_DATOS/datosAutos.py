from faker import Faker
from time import time


fake = Faker()
tiempo = time()
print("AUTOS")
print("insert into choques (id_auto, largo, ancho, alto, peso_neto, peso_max, tipo_combustible, tipo_auto, cant_pasajero, numeroAro) values")

while (x<10):
    print("({},'{}','{}','{}'),
    ".format(x,fake.name(),fake.address(), fake.email(),fake.url()))
    x = x+1
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)