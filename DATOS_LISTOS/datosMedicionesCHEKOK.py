from random import choice, random, randint, randrange
from configuraciones import *
import psycopg2

conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


sql="""select id_sensor from sensores;"""
cur.execute(sql)
posts  = cur.fetchall()
sql="""select patente from autos;"""
cur.execute(sql)
posts2  = cur.fetchall()

c=1
for t in posts2:
    fecha=43438
    for x in range(10):
        hour=choice(('12:','13:','15:','16:'))    
        for w in range(20,60):
            last=hour
            hour+=str(w)
            for y in posts:
                if y[0] == 1:
                    data=randrange(80,160,5)
                if y[0] == 2:
                    data=randrange(70,180,2)
                if y[0] == 3:
                    data=randrange(130, 280,5)
                if y[0] == 4:
                    data=randrange(10,37,1)
                if y[0] == 5:
                    data=randrange(30,80,10)
                if y[0] == 6:
                    data=randrange(12,15,1)
                if y[0] == 7:
                    data=randrange(60, 150, 10)
                if y[0] == 8:
                    data=randrange(50,120,5)           
                sql="""insert INTO mediciones VALUES"""
                sql=sql+("('{}','{}','{}','{}','{}');".format(y[0],
                t[0],
                hour,
                fecha,
                data))
                cur.execute(sql)
                c+=1
            hour=last
        fecha+=1

conn.commit()
cur.close()
conn.close()