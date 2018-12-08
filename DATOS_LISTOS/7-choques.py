from faker import Faker
from random import choice, random, randint
import csv
from configuraciones import *
import psycopg2




results = ["Gran Santiago","Gran Concepcion","Gran Valparaiso",
"Gran La Serena","Antofagasta","Gran Temuco",
"Gran Rancagua","Gran Iquique","Talca",
"Arica","Gran Puerto Montt","Gran Chillan","Los Angeles",
"Calama","Calama","Copiapo","Osorno","Gran Quillota",
"Valdivia","Punta Arenas","Gran San Antonio",
"Curico","Ovalle","Linares","Los Andes",
"Melipilla","San Felipe"]


santiago = []
concepcion = []
valparaiso = []
serena = []
antofagasta = []
temuco = []
rancagua = []
iquique = []
talca = []
arica = []
puertomontt = []
chillan = []
angeles = []
calama = []
copiapo = []
osorno = []
quillota = []
valdivia = []
puntaarenas = []
sanantonio = []
curico = []
ovalle = []
linares = []
andes = []
melipilla = []
sanfelipe = []


with open('Ciudades.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        santiago.append(row['Gran Santiago'])
        concepcion.append(row['Gran Concepcion'])
        valparaiso.append(row['Gran Valparaiso'])
        serena.append(row['Gran La Serena'])
        antofagasta.append(row['Antofagasta'])
        temuco.append(row['Gran Temuco'])
        rancagua.append(row['Gran Rancagua'])
        iquique.append(row['Gran Iquique'])
        talca.append(row['Talca'])
        arica.append(row['Arica'])
        puertomontt.append(row['Gran Puerto Montt'])
        chillan.append(row['Gran Chillan'])
        angeles.append(row['Los Angeles'])
        calama.append(row['Calama'])
        copiapo.append(row['Copiapo'])
        osorno.append(row['Osorno'])
        quillota.append(row['Gran Quillota'])
        valdivia.append(row['Valdivia'])
        puntaarenas.append(row['Punta Arenas'])
        sanantonio.append(row['Gran San Antonio'])
        curico.append(row['Curico'])
        ovalle.append(row['Ovalle'])
        linares.append(row['Linares'])
        andes.append(row['Los Andes'])
        melipilla.append(row['Melipilla'])
        sanfelipe.append(row['San Felipe'])


calles = {}
calles['Gran Santiago'] = santiago
calles['Gran Concepcion'] = concepcion
calles['Gran Valparaiso'] = valparaiso
calles['Gran La Serena'] = serena
calles['Antofagasta'] = antofagasta
calles['Gran Temuco'] = temuco
calles['Gran Rancagua'] = rancagua
calles['Gran Iquique'] = iquique
calles['Talca'] = talca
calles['Arica'] = arica
calles['Gran Puerto Montt'] = puertomontt
calles['Gran Chillan'] = chillan
calles['Los Angeles'] = angeles
calles['Calama'] = calama
calles['Copiapo'] = copiapo
calles['Osorno'] = osorno
calles['Gran Quillota'] = quillota
calles['Valdivia'] = valdivia
calles['Punta Arenas'] = puntaarenas
calles['Gran San Antonio'] = sanantonio
calles['Curico'] = curico
calles['Ovalle'] = ovalle
calles['Linares'] = linares
calles['Los Andes'] = andes
calles['Melipilla'] = melipilla
calles['San Felipe'] = sanfelipe 



conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


fake = Faker()

for x in range(0,10):
    ciudad = choice(results)
    fecha = fake.date()
    hora = fake.time() 
    sql = ("""insert into choques (ID_EVENTO,fecha,hora,ciudad,calle,numeracion) values""")
    sql = sql + ("({},'{}','{}','{}','{}','{}');".format(x,
    fecha,
    hora,
    ciudad,
    choice(calles[ciudad]),
    str(randint(0,9999))))

    cur.execute(sql)

conn.commit()
cur.close()
conn.close()