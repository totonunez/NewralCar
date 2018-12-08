from time import time
from random import choice, randint, randrange
from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql="""select rut from clientes;"""

cur.execute(sql)
posts  = cur.fetchall()


#print(posts)

tiempo = time()
combustible = ["gasolina98", "gasolina95", "gasolina93", "Diesel"]
tautos = ["Sedan", "Station Wagon", "Doble Cabina", "Hatchback","SUV", "Furgon"]

def rand():
    return choice(['A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','I','O','P','Q'])
def rand2():
    return randrange(1,9,1)

list1=[]

#print("insert into autos (patente, largo, ancho, alto, peso_neto, peso_max, tipo_combustible, tipo_auto, cant_pasajero, numeroAro) values")
#patente, rut, largo , ancho, alto, peso_neto, tipo_combustible, tipo_auto, maximo_pasajeros, num_aro
for x in posts:
    peso_neto = randint(2700, 3860)
    patente=str(rand())+str(rand())+str(rand())+str(rand())+str(rand2())+str(rand2())
    while patente in list1:
        patente=str(rand())+str(rand())+str(rand())+str(rand())+str(rand2())+str(rand2())
    list1.append(patente)
    sql="""insert into autos (patente,rut,largo,ancho,alto,peso_neto,tipo_combustible,tipo_auto,maximo_pasajeros,num_aro) values """
    sql=sql+("('{}',{},{},{},{},{},'{}','{}',{},'{}');".format(patente,
    x[0],
    randint(3500, 5000),
    randint(1700, 1900), 
    randint(1300, 1800),
    peso_neto + randint(500, 1000), 
    choice(combustible), 
    choice(tautos), 
    choice([2,4,6]), 
    choice(['Aro 24','Aro 26','Aro 28'])))
    #print(sql)
    cur.execute(sql)

conn.commit()
cur.close()
conn.close()
