from random import choice
from faker import Faker
import time
from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()



fake = Faker()


print("INVOLUCRADOS")
print("insert into involucrados (id_auto, id_choque , numero_de_afectados) values (")

for x in range(0,5):
    for y in range(0,5):
        print("({},'{}','{}'),".format(x,y,choice([1,2,3,4,5,6])))
print(")")

conn.commit()
cur.close()
conn.close()
