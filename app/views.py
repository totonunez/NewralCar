from app import app
from flask import render_template,request,redirect
from configuraciones import *

import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
	
	sql ="""
	select count(*) from autos;
	"""
	print sql 
	cur.execute(sql)
	cantidad_auto  = cur.fetchall()

	return render_template("index.html",cantidad_auto=cantidad_auto)


@app.route('/ELIMINAR',methods=['GET', 'POST'])
def borrar():
	return render_template("eliminar_inicio.html",nombre="nombre")


@app.route('/ELIMINAR_AUTO',methods=['GET', 'POST'])
def borrarauto():
	if request.method == 'POST':
		patente =  request.form['PATENTE']
		try:
			sql= """delete from mediciones where mediciones.patente='%s';"""%(patente)
			print(sql)
			print(cur.execute(sql))
			sql= """delete from autos where autos.patente ='%s';""" %(patente)
			print(cur.execute(sql))
			print(sql)
			return render_template("eliminacion_ok.html",nombre="nombre")
		except:
			print("error")
			return render_template("eliminar_error.html",nombre="nombre")
	else:
		return render_template("eliminar_auto.html",nombre="nombre")



@app.route('/ELIMINAR_CLIENTE',methods=['GET', 'POST'])
def borrarcliente():
	if request.method == 'POST':
		rutcliente = request.form['RUT']
		print("se procede a eliminar el cliente",rutcliente)
		try:
			print("sql lo intenta")
			sql= """ delete from clientes where clientes.rut = %s"""%(rutcliente)
			x=cur.execute(sql)
			print(x)
			if x is None:
				print("sql falla")
				return render_template("eliminar_error.html",nombre="nombre")
			sql= """ delete from autos where autos.rut = %s"""%(rutcliente)
			print(cur.execute(sql))
			conn.commit()
			return render_template("eliminacion_ok.html",nombre="nombre")
		except:
			return render_template("eliminar_error.html",nombre="nombre")
	else:
		return render_template("eliminar_cliente.html",nombre="nombre")


@app.route('/ELIMINAR_DEBE',methods=['GET', 'POST'])
def borrardebe():
	if request.method == 'POST':
		iddebe = request.form['ID']
		try:
			sql= """delete from debe where debe.id_penalizacion = %s"""%(iddebe)
			cur.execute(sql)
			conn.commit
			return render_template("eliminacion_ok.html",nombre="nombre")
		except:
			return render_template("eliminar_error.html",nombre="nombre")
	else:
		return render_template("eliminar_debe.html",nombre="nombre")


@app.route('/ACTUALIZAR', methods=['GET','POST'])
def actualizar():
	return render_template('actualizar_inicio.html')

@app.route('/ACTUALIZAR_DUENO',methods=['GET','POST'])
def actualizardueno():
	if request.method == 'POST':
		rutdueno = resquest.form['RUT']
		patente2 = request.form['PATENTE']
		try:
			sql= """update set auto.montrut = %s, from autos where autos.patente = %s """%(rutdueno,patente2)
			cur.excecute(sql)
			conn.commit()
			return render_template("eliminacion_ok.html",nombre="nombre")
		except:
			return render_template("eliminar_error.html",nombre="nombre")
	else:
		return render_template("actualizar_dueno.html",nombre="nombre")


@app.route('/ACTUALIZAR_FECHADEBE',methods=['GET','POST'])
def actualizardebe():
	if request.method == 'POST':
		rutdebe = resquest.form['RUT']
		fecha = request.form['FECHA_VENC']
		try:
			sql= """update set auto.fecha_vencimiento = %s, from autos where autos.patente = %s """%(fecha,rutdebe)
			cur.excecute(sql)
			conn.commit()
			return render_template("eliminacion_ok.html",nombre="nombre")
		except:
			return render_template("eliminar_error.html",nombre="nombre")
	else:
		return render_template("actualizar_dueno.html",nombre="nombre")	

@app.route('/ACTUALIZAR_TELEFONO',methods=['GET','POST'])
def actualizartelefono():
	if request.method == 'POST':
		ruttel = resquest.form['RUT']
		telefono = request.form['TELEFONO']
		try:
			sql= """update set clientes.rut = %s, from clientes where clientes.patente = %s """%(ruttel,telefono)
			cur.excecute(sql)
			conn.commit()
			return render_template("eliminacion_ok.html",nombre="nombre")
		except:
			return render_template("eliminar_error.html",nombre="nombre")
	else:
		return render_template("actualizar_dueno.html",nombre="nombre")	

@app.route('/CREAR',methods=['GET','POST'])
def crear():
	return render_template('crear_inicio.html')

@app.route('/CREAR_SENSOR',methods=['GET','POST'])
def crearsensor():
	if request.method == 'POST':
		idsensor = resquest.form['ID_SENSOR']
		nombresensor = request.form['NOMBRE']
		presicion = request.form['PRESICION']
		unidad = request.form['TIPO_UNIDAD']
		try:
			sql= """insert into sensores values(%s, %s, %s, %s) """%(idsensor, nombresensor, presicion, unidad)
			cur.excecute(sql)
			conn.commit()
			return render_template("eliminacion_ok.html",nombre="nombre")
		except:
			return render_template("eliminar_error.html",nombre="nombre")
	else:
		return render_template("actualizar_dueno.html",nombre="nombre")




@app.route('/formularios', methods=['GET', 'POST'])
def formularios():
	if request.method == 'POST':
		variable =  request.form['toto']
		sql = """insert into comentarios (post_id,usuario_id,comentario)
		values (1,1,'%s')
		 """%(variable)
		cur.execute(sql)
		conn.commit()

	return render_template("forms.html",nombre="nombre")

@app.route('/tablas')
def tablas():
	return render_template("tables.html",nombre="nombre")
