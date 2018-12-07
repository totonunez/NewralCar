from faker import Faker
from time import time 
from random import random, choice
from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()

sql="""select patente from autos;"""
cur.execute(sql)
posts  = cur.fetchall()

for a in posts:
    c=choice([0,1])
    fecha = 43438 
    for x in range (10):
        hour = choice(['12:','13:','15:','16:'])
        for w in range(20,60):
            if c is 1:
                iniciolatitud=-70.599644
                iniciolongitud=-33.490855
                for i in range(2000):
                    last = hour
                    hour += str(w)
                    sql = """ insert into gps (PATENTE,fecha,hora,longitud,latitud) values  """
                    sql = sql +("('{}','{}','{}',{},{})".format(a[0],
                    fecha,
                    hour,
                    iniciolongitud-i*0.0000001,
                    iniciolatitud-i*0.00001))
                    cur.execute(sql)
            if c is 2:
                iniciolatitud=-70.539405
                iniciolongitud=-33.428637
                for i in range(4000):
                    last = hour
                    hour += str(w)
                    sql = """ insert into gps (PATENTE,fecha,hora,longitud,latitud) values """
                    sql = sql +("('{}','{}','{}',{0:.6f},{0:.6f})".format(a[0],
                    fecha,
                    hour,
                    iniciolongitud-i*0.0000001,
                    iniciolatitud-i*0.00001))
                    cur.execute(sql)
            hour=last
        fecha +=1







conn.commit()
cur.close()
conn.close()