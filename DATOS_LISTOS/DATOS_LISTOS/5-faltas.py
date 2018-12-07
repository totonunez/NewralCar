from faker import Faker
from time import time
from random import choice, random, randint
from configuraciones import *
from datetime import datetime, timedelta
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


fake = Faker()

for x in range(0,10):
    plata = randint(40000,300000) 
    sql="""insert into faltas (id_penalizacion,monto,comentario) values"""
    sql = sql + ("({},{},'{}')".format(x,
    (plata - plata%1000),
    fake.text()))
    cur.execute(sql)

conn.commit()
cur.close()
conn.close()
