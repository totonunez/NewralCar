from faker import Faker
from time import time
from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()

fake = Faker()

sql="""select rut from clientes;"""
cur.execute(sql)
posts  = cur.fetchall()

sql="""select id_penalizacion from faltas;"""
cur.execute(sql)
posts2  = cur.fetchall()


for x in posts:
    faltasdebidas = []
    for y in range (0,randint(0,randint(0,10))):
        faltita = choice(posts2)[0]
        while faltita in faltasdebidas:
            faltita = choice(posts2)[0]
        faltasdebidas.append(faltita)
        
        fechaIncidente = fake.date()
        fechaPago = fake.date()
        while fechaIncidente > fechaPago:
            fechaPago = fake.date()
        sql= ("""insert into debe values""")
        sql = sql + ("({},{},'{}','{}');".format(x[0],faltita,fechaIncidente,fechaPago))
        cur.execute(sql)


conn.commit()
cur.close()
conn.close()
