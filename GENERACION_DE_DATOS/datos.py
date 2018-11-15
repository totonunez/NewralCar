from faker import Faker
from time import time
fake = Faker()
hola = time()
for i in range(10):

    print(fake.name()," ",fake.email())
lapsoTiempo = time() - hola
print(lapsoTiempo)

w