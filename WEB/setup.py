from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()



sql ="""DROP SCHEMA public CASCADE; CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE CLIENTES
           (RUT integer PRIMARY KEY,
           digito varchar(10),
           nombre varchar(100),
           apellido varchar(100),
           email varchar(100),
           telefono varchar(100),
           url varchar(100));
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
            num_aro varchar);
"""
cur.execute(sql)


sql ="""
CREATE TABLE SENSORES
           (id_sensor int PRIMARY KEY, 
           nombre varchar(40), 
           presicion integer, 
           tipo_unidad varchar(10));
"""

cur.execute(sql)



sql ="""
CREATE TABLE MEDICIONES
           (id_sensor int references SENSORES(id_sensor),
            PATENTE varchar(6) references AUTOS(PATENTE),
            hora varchar(10),
            fecha varchar(20),
            valor int,
            longitud int,
            latitud int);
"""
cur.execute(sql)

sql ="""
CREATE TABLE CHOQUES
            (ID_EVENTO int PRIMARY KEY,
            fecha varchar(20),
            hora varchar(10),
            ciudad varchar(60),
            calle varchar(60),
            numeracion varchar(10));
"""
cur.execute(sql)

sql ="""
CREATE TABLE INVOLUCRADOS
            (ID_EVENTO int references CHOQUES(ID_EVENTO),
            PATENTE varchar(6) references AUTOS(PATENTE),
            pasajeros_afectados int);
"""
cur.execute(sql)


sql ="""
CREATE TABLE FALTAS
            (id_penalizacion integer PRIMARY KEY,
            monto int,
            comentario varchar(300));
"""
cur.execute(sql)

sql ="""
CREATE TABLE DEBE
            (RUT integer references CLIENTES(RUT),
            fecha_incidente varchar(20),
            fecha_vencimiento varchar(20),
            id_penalizacion integer references FALTAS(id_penalizacion));
"""
cur.execute(sql)



conn.commit()
cur.close()
conn.close()
