from faker import Faker
from time import time 

fake = Faker()
tiempo = time()

x = 1
print("CLIENTES")
print("insert into choques (id_usuario, nombre, apellido, direccion, correo, celular, foto, fecha_nacimiento) values")

for x in range(0,10):
    y = fake.name()
    print("({},'{}','{}','{}','{}','{}','{}','{}'),".format(x,y.split()[0],y.split()[1],fake.address(), fake.email(),fake.phone_number(),fake.url(),fake.date()))

print(")")

final = time()- tiempo
print "Tiempo total en crearse todos los datos es" , final










