from faker import Faker
from time import time 

fake = Faker()
tiempo = time()
from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


print("MEDICIONES")
print("insert into choques (id_sensores,id_auto, id_registro) values")
for x in range(0,10):
    for y in range(0,5):
        for z in range(0,5):
            print("({},'{}','{}'),".format(x,y,z))
            sql="""insert into choques (%s,%s,%s) values;"""%(x,y,z)
            cur.execute(sql)
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)
