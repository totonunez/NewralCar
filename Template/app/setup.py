from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE posts 
           (id serial PRIMARY KEY, titulo varchar(40), resumen varchar, texto text, creado timestamp);
"""

cur.execute(sql)


sql ="""
CREATE TABLE categorias 
           (id serial PRIMARY KEY, nombre varchar(40), creado timestamp);
"""

cur.execute(sql)

sql ="""
CREATE TABLE categorias_posts 
           (categoria_id integer, post_id integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE  usuarios
           (id serial PRIMARY KEY,rol integer, nombre varchar(40),apellido varchar(40),
           email varchar(100),passwd varchar(255), creado timestamp);
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