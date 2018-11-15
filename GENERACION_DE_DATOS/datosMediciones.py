from faker import Faker
from time import time 

fake = Faker()
tiempo = time()

print("MEDICIONES")
print("insert into choques (id_sensores,id_auto, id_registro) values")
while (x<10):
    print("({},'{}','{}','{}'),
    ".format(x,fake.name(),fake.address(), fake.email(),fake.url()))
    x = x+1
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)