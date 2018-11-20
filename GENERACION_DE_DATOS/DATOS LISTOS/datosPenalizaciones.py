from faker import Faker
from time import time
from random import choice, random, randint
from datetime import datetime, timedelta

fake = Faker()
tiempo = time()
print("PENALIZACION")
print("insert into choques (id, monto, fecha_incidente, fecha_Pago) values")
for x in range(0,10):
    incidente = fake.date()
    pago = fake.date()
    while incidente > pago:
        pago = fake.date()

    print("('{}','{}','{}','{}'),".format(x,randint(40000,300000),incidente,pago))
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)