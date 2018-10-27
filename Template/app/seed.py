from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into categorias (nombre) values ('Tecnologia '),('Video Juegos '),('Geek'),
('Cine'),('Mundo Marvel');
"""
cur.execute(sql)
sql ="""
insert into posts (titulo,resumen,texto,creado) values ('Iron Man 4 ','La nueva pelicula de iron saldra el proximo 2018',
'Esta pelicula bla bla bla y ser la mejor por que si ',now()) returning id;
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
