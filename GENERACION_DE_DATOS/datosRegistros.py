from faker import Faker
from time import time
from random import choice, random, randint


fake = Faker()
tiempo = time()

print("REGISTROS")
print("insert into choques (id_registro, hora, fecha, magnitud) values")

for x in range(0,10):
    print("({},'{}','{}','{}'),".format(x,fake.date(), fake.time(),randint(0,1023)))
print(")")
final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)