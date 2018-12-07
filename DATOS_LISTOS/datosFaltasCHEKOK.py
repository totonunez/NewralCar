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
    fechaIncidente = fake.date()
    fechaPago = fake.date()
    while fechaIncidente > fechaPago:
        fechaPago = fake.date()

    sql="""insert into faltas (id_penalizacion,monto,comentario,fecha_incidente,fecha_vencimiento) values"""
    sql = sql + ("({},{},'{}','{}','{}')".format(x,
    randint(40000,300000),
    fake.text(),
    fechaIncidente,
    fechaPago))
    cur.execute(sql)

conn.commit()
cur.close()
conn.close()
