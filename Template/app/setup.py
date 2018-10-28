from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()



sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;""" #Esta linea eliminará todas las tablas creadas en la base de datos

cur.execute(sql) #ejecutar la accion anterior

sql ="""
CREATE TABLE autos 
           (patente PRIMARY KEY, largo varchar(40), ancho varchar, alto text, creado timestamp, peso_neto, peso_max, tipo_combustible, tipo_auto, cant_pasajeros, NumeroAro);
"""

cur.execute(sql)


sql ="""
CREATE TABLE choques 
           (id_evento PRIMARY KEY, ciudad varchar(40), creado timestamp);
"""

cur.execute(sql)

sql ="""
CREATE TABLE categorias_posts 
           (categoria_id integer, post_id integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE  cliente
           (id serial PRIMARY KEY,rol integer, nombre varchar(40),apellido varchar(40),
           email varchar(100),foto jpg,fecha_nacimiento, creado timestamp);
"""

cur.execute(sql)

sql ="""
CREATE TABLE comentarios
           (id serial PRIMARY KEY, comentario varchar(140), post_id integer, usuario_id integer, creado timestamp);
"""

cur.execute(sql)


conn.commit()
cur.close()
conn.close()