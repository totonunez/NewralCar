from random import choice, random, randint, randrange
from configuraciones import *
import psycopg2
import time
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


sql="""select id_sensor from sensores;"""
cur.execute(sql)
posts  = cur.fetchall()
sql="""select patente from autos;"""
cur.execute(sql)
posts2  = cur.fetchall()
t=[]

c=1
while True:
    aux=choice(posts2)
    if aux in t:
        break
    t.append(aux)
    fecha=48888

    for x in range(3):
        hour=choice(('06:','05:','22:','21:'))
        iniciolongitud=choice((-22.192995,-22.467902,-22.657025,-22.467987,-22.454815,-22.562317,-22.993245,-22.301684))
        iniciolatitud=choice((-68.210644,-68.037475,-68.129324,-68.398342,-68.645464,-68.969405,-68.759644,-68.544567))
        c=1
        for w in range(25,39):
            last=hour
            hour+=str(w)
            lon=str(iniciolongitud-c*0.000001)
            lat=str(iniciolatitud-c*0.00001)
            c+=1
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
                if y[0] == 9:
                    data=randrange(60, 150, 10)
                if y[0] == 10:
                    data=randrange(60, 150, 10)
                sql="""insert INTO mediciones VALUES"""
                sql=sql+("('{}','{}','{}','{}','{}','{}','{}');".format(y[0],
                t[0],
                hour,
                fecha,
                data,lon,lat))
                cur.execute(sql)
                print 'nuevo data de: '
                print sql
                time.sleep(0.5)
                c+=1
            hour=last
        fecha+=1

conn.commit()
cur.close()
conn.close()