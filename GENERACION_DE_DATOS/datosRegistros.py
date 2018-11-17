from faker import Faker
from time import time
from datetime import datetime, timedelta, date, time
from random import choice, random


fake = Faker()
tiempo = time()
inicio = datetime(2010,1,1)
fin    = datetime(2018,11,16)
lista_fechas = [(inicio + timedelta(days=d)).strftime("%Y-%m-%d")
                    for d in range((fin - inicio).days + 1)] 

print("REGISTROS")
print("insert into choques (id_registro, hora, fecha, magnitud) values")

for count in range(0,10):
    print ("({},'{}','{}','{}'),".format(count,fake.name(), choice(lista_fechas),random.random())

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)