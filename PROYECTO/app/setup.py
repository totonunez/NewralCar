from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()



sql ="""DROP SCHEMA public CASCADE; CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE CLIENTES
           (RUT integer PRIMARY KEY,
           digito varchar(1),
           nombre varchar(40),
           apellido varchar(40),
           email varchar(100),
           telefono varchar(10), 
           creado timestamp);
"""
cur.execute(sql)

sql ="""
CREATE TABLE AUTOS
           (PATENTE varchar(6) PRIMARY KEY,
            rut integer references clientes(rut),
            largo integer, 
            ancho integer, 
            alto integer, 
            peso_neto integer,
            tipo_combustible varchar, 
            tipo_auto varchar, 
            maximo_pasajeros integer,
            num_aro varchar, 
            creado timestamp);
"""
cur.execute(sql)


sql ="""
CREATE TABLE SENSORES
           (id_sensor varchar(10) PRIMARY KEY, 
           nombre varchar(40), 
           presicion integer, 
           tipo_unidad varchar(10),
           creado timestamp);
"""

cur.execute(sql)



sql ="""
CREATE TABLE MEDICIONES
           (id_sensor varchar(10) references SENSORES(id_sensor),
            patente varchar(6) references AUTOS(PATENTE),
            hora int,
            fecha int,
            valor int,
            creado timestamp);
"""
cur.execute(sql)

sql ="""
CREATE TABLE CHOQUES
            (ID_EVENTO int PRIMARY KEY,
            fecha int,
            hora int,
            ciudad varchar(60),
            calle varchar(60),
            numeracion varchar(10),
            creado timestamp);
"""
cur.execute(sql)

sql ="""
CREATE TABLE INVOLUCRADOS
            (ID_EVENTO int references CHOQUES(ID_EVENTO),
            PATENTE varchar(6) references AUTOS(PATENTE),
            numero_afectados int,
            creado timestamp);
"""
cur.execute(sql)

sql ="""
CREATE TABLE GPS
            (PATENTE varchar(6) references AUTOS(PATENTE),
            fecha int,
            hora int,
            longitud int,
            latitud int,
            creado timestamp);
"""
cur.execute(sql)

sql ="""
CREATE TABLE FALTAS
            (id_penalizacion integer PRIMARY KEY,
            monto int,
            comentario varchar(100),
            fecha_incidente int,
            fecha_vencimiento int,
            creado timestamp);
"""
cur.execute(sql)

sql ="""
CREATE TABLE DEBE
            (RUT integer references CLIENTES(RUT),
            id_penalizacion integer references FALTAS(id_penalizacion),
            creado timestamp);
"""
cur.execute(sql)



conn.commit()
cur.close()
conn.close()
