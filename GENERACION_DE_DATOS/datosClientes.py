from faker import Faker
from time import time 

fake = Faker()
tiempo = time()

print(fake.name())
x = 1
print("CLIENTES")
print("insert into choques (id_usuario, nobre, apellido, correo, celular, foto, fecha_nacimiento) values")

while (x<10):
    print("({},'{}','{}','{}'),
    ".format(x,fake.name(),fake.address(), fake.email(),fake.url()))
    x = x+1
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)










