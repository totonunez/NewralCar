from faker import Faker
from time import time 
from random import choice

fake = Faker()
tiempo = time()
list3=['1','2','3','6','8','k','0']


x = 1
print("CLIENTES")
print("insert into clientes (id_usuario, digito, nombre, apellido, email, telefono, direccion) values")

for x in range(0,10):
    y = fake.name()
    print("({},'{}','{}','{}','{}','{}','{}'),".format(x,choice(list3),y.split()[0],y.split()[1], fake.email(),fake.phone_number(),fake.address()))
print(")")











