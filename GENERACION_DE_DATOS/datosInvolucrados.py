from faker import Faker
from time import time 

fake = Faker()
tiempo = time()

print("INVOLUCRADOS")
print("insert into involucrados (id_auto, id_choque, hora, fecha, numero_de_afectados) values")

while (x<10):
    print("({},'{}','{}','{}'),".format(x,fake.name(),fake.address(), fake.email(),fake.url()))
    x = x+1
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)
