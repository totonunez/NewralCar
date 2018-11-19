from faker import Faker
from time import time 

fake = Faker()
tiempo = time()

x = 1
print("CLIENTES")
print("insert into choques (id_usuario, nombre, apellido, direccion, correo, celular, foto, fecha_nacimiento) values")

while (x<10):
    y = fake.name()
    a,b=y.split()
    print("('{}','{}','{}','{}'),".format(x,a,b,fake.address(), fake.email(),fake.url(),fake.date()))
    x = x+1

print(")")

final = time()- tiempo
print "Tiempo total en crearse todos los datos es" , final










