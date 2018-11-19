from random import choice
from faker import Faker
import time


fake = Faker()


print("INVOLUCRADOS")
print("insert into involucrados (id_auto, id_choque, hora, fecha , numero_de_afectados) values")

for x in range(0,5):
    for y in range(0,5):
        print("({},'{}','{}','{}','{}'),".format(x,y,fake.date(),fake.time(),choice([1,2,3,4,5,6])))
print(")")