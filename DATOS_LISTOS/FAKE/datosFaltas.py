from faker import Faker
from time import time
from random import choice, random, randint
from datetime import datetime, timedelta

fake = Faker()

print("PENALIZACION")
print("insert into choques (id_penalizacion, monto, fecha_incidente, fecha_vencimiento) values")
for x in range(0,10):
    incidente = fake.date()
    pago = fake.date()
    while incidente > pago:
        pago = fake.date()

    print("({},{},'{}','{}','{}'),".format(x,randint(40000,300000),fake.text(),incidente,pago))
print(")")