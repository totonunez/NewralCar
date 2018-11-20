from faker import Faker
from time import time
from random import choice, random, randint
from datetime import datetime, timedelta

fake = Faker()
tiempo = time()
print("PENALIZACION")
print("insert into choques (id, monto, fecha_incidente, fecha_Pago) values")
while (x<10):
    fecha = fake.date()
    print("('{}','{}','{}','{}'),".format(x,randint(40000,300000),fecha,))
    x = x+1
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)

print("EL TOTO TIENE BONITOS DE COLOR DE PIEL, OJOS, y COLOR y VOZ")