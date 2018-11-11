from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()



sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;""" #Esta linea eliminará todas las tablas creadas en la base de datos

cur.execute(sql) #ejecutar la accion anterior

sql ="""
CREATE TABLE autos
           (id_auto serial PRIMARY KEY, largo varchar(40), ancho varchar, alto varchar, peso_neto varchar,
 peso_maximo varchar , tipo_combustible varchar, tipo_auto varchar, maximo_pasajeros varchar,
 num_aro varchar, texto text, creado timestamp);
"""

cur.execute(sql)

sql ="""
CREATE TABLE mediciones
           ( id_sensor, id_auto, fecha, hora serial PRIMARY KEY, magnitud varchar(40), creado timestamp);
"""

cur.execute(sql)

sql ="""
CREATE TABLE sensores
           (id_sensor serial PRIMARY KEY, nombre varchar(40), presicion integer, creado timestamp);
"""

cur.execute(sql)

sql ="""
CREATE TABLE clientes
           (id_usuario serial PRIMARY KEY, nombre varchar(40),apellido varchar(40),
           email varchar(100),passwd varchar(255),celular intiger, foto png, creado timestamp);
"""

cur.execute(sql)

sql ="""
CREATE TABLE penalizaciones
           (id_penalizacion serial PRIMARY KEY), monto integer, comentario integer, fecha_incidente date,
fecha_pago date, creado timestamp;
"""

cur.execute(sql)

sql = """
CREATE TABLE involucrados
           (id_auto, id_choque, fecha ,hora serial PRIMERARY KEY), numero_de_afectados, creado timestap

"""

cur.execute(sql)

sql= """
CREATE TABLE debe
           (id_usuario, id_penalizacion serial PRIMARY KEY), comentario varchar(140),creado timestap

"""

cur.execute(sql)

sql = """
CREATE TABLE choques
           (id_evento serial PRIMARY KEY), ciudad varchar(40), calle varchar, numeracion intiger, creado timestap

"""
cur.execute(sql)

sql = """
CREATE TABLE GPS
           (id_auto, fecha, hora serial PRIMARY KEY), latitud varchar(40), longitud varchar, creado timestap

"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()
