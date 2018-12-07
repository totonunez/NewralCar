from random import choice, random
from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


seq=["Sensor De Presion Cilindros",
"Sensor Temperatura Radiador",
"Sensor Temperatura Cilindros",
"Sensor Temperatura Interior",
"Sensor Presion Aire",
"Sensor Voltaje Bateria",
"Sensor Velocidad",
"Sensor De Aceleracion"]

presicion=['0.9','0.92','0.93', '1.00']
seq2=['atms',
'celsius',
'celsius',
'celsius',
"atms",
"volt",
"ms",
"ms2"]
x=1
for i in seq:
    sql="""insert into sensores (id_sensor, nombre,presicion,tipo_unidad) values"""
    sql=sql+("('{}','{}',{},'{}');".format(x, 
    i,
    choice(presicion), 
    seq2[x-1]))
    x=x+1
    cur.execute(sql)

conn.commit()
cur.close()
conn.close()
