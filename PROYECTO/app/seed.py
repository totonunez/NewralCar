from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into choques (id_evento, ciudad,calle, numeracion, fecha, hora) values
(0,'Gran Puerto Montt','San Ignacio','1930','1978-08-20','21:13:37'),
(1,'Gran Rancagua','Av.Republica de Chile','1035','1990-11-20','18:29:32'),
(2,'Osorno','Alcalde Rene Soriano Borquez','2713','1999-04-11','04:03:06'),
(3,'Gran Quillota','Ramon Freite','2935','1995-09-28','13:46:27'),
(4,'Linares','Arturo Prat','327','1995-09-09','13:25:38'),
(5,'Curico','Argomedo','2004','1973-12-14','11:40:37'),
(6,'Curico','Argomedo','1786','2001-04-29','20:43:20'),
(7,'Gran Quillota','Av. Condell','1196','1983-07-26','12:04:21'),
(8,'Gran Puerto Montt','Regimiento','695','1984-04-26','23:09:21'),
(9,'Linares','Valentin Letelier','819','1986-12-24','20:59:23'), now());

"""
cur.execute(sql)

sql ="""
insert into choques (id_evento, ciudad,calle, numeracion, fecha, hora) values
(0,'Los Andes','Esmeralda','517','1986-11-11','17:32:53'),
(1,'Arica','Linderos','877','2003-10-21','01:27:04'),
(2,'Calama','Av. Grecia','2009','1982-10-07','04:25:38'),
(3,'Arica','Gonzalo Cerda','637','1991-10-29','14:08:03'),
(4,'San Felipe','Hnos Carrera','2973','1986-03-30','04:14:32'),
(5,'Talca','Cancha Rayada','1379','1994-08-16','16:44:12'),
(6,'Osorno','Cesar Ercilla','2436','1996-02-08','18:41:40'),
(7,'Calama','Av. Grecia','1349','1976-04-05','09:33:14'),
(8,'Antofagasta','Maipu','217','1987-07-04','17:58:57'),
(9,'Gran Rancagua','Av. Capitan Ramon Freire','984','2015-01-07','23:21:08'))
"""
cur.execute(sql)

conn.commit()
post_id = cur.fetchone()[0]

print post_id


sql ="""insert INTO categorias_posts (categoria_id,post_id)
(SELECT id,%i  FROM categorias where nombre = 'Cine' or 
 nombre = 'Geek' or 
  nombre = 'Mundo Marvel'
);"""%(post_id)

cur.execute(sql)


sql ="""insert INTO usuarios (nombre,apellido,email,passwd,creado)
 values ('Manuel','Alba','malba@mmae.cl','1234',now() );
"""

cur.execute(sql)



conn.commit()
cur.close()
conn.close()
