from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into clientes (id_usuario, digito, nombre, apellido, email, telefono, direccion) values
(
(0,'3','Anna','Davis','sonya44@hotmail.com','803.988.0742x42848','9278 Pamela Village Suite 025
Mccormicktown, RI 08538'),
(1,'0','Aaron','Cruz','garrettlindsey@ramsey.com','(865)122-6743x7352','2219 Harrington Ramp Apt. 397
Thomasfort, NM 35835'),
(2,'6','Henry','Thompson','john25@coleman-howard.net','053.959.5002x2763','USCGC Campbell
FPO AA 51237'),
(3,'6','Tina','Bentley','pamela22@lamb-brown.info','001-333-172-8594x703','723 Jackson Land
North Philipstad, NY 87450'),
(4,'8','Amber','Davis','jermainevance@page.org','001-984-233-1157','0412 Craig Course
South Juan, UT 17560'),
(5,'6','Alejandro','Bowman','waltersmichael@hotmail.com','+1-506-627-3631','084 Paige Hills Suite 051
South Brian, VA 33707'),
(6,'0','Sandra','Mccarty','suttonshannon@sanchez-stewart.com','9716512299','5466 Garcia Squares Suite 206
Port Keith, ND 52525'),
(7,'3','Kimberly','Lindsey','james32@gmail.com','438.926.9177','97554 Lisa Flats
Lake Robertshire, GA 04207'),
(8,'k','Lisa','Medina','princelauren@hernandez.com','710.179.5736x630','PSC 5488, Box 9200
APO AA 20188'),
(9,'6','Christopher','Powell','lyonsbrooke@gmail.com','148.727.2822','75097 Mckinney Key Suite 431
East Paul, OR 06241')
)

"""
cur.execute(sql)


'''

conn.commit()
post_id = cur.fetchone()[0]

print post_id

sql ="""insert INTO categorias_posts (categoria_id,post_id)
(SELECT id,%i  FROM categorias where nombre = 'Cine' or 
 nombre = 'Geek' or 
  nombre = 'Mundo Marvel'
);"""%(post_id)

cur.execute(sql)

'''
conn.commit()
cur.close()
conn.close()
