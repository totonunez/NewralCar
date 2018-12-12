from app import app
from flask import render_template,request,redirect
from configuraciones import *

import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
	try:
		sql ="""
		select count(*) from autos;
		"""
		print sql 
		cur.execute(sql)
		cantidad_auto  = cur.fetchall()
		conn.commit()

		sql ="""
		select count(*) from clientes;
		"""
		print sql 
		cur.execute(sql)
		cantidad_clientes  = cur.fetchall()
		conn.commit()

		sql = """select choques.calle, choques.numeracion, choques.fecha, choques.hora 
		from choques,(select count(*) as cantidad, id_evento from involucrados group by id_evento) as kk 
		where kk.cantidad  = (select max(cosas) 
								from (select count(*) as cosas 
										from involucrados group by id_evento) as jj) and choques.id_evento = kk.id_evento;"""

		print sql
		cur.execute(sql)
		granchoque = cur.fetchall()
		conn.commit()
	except expression as identifier:
		pass
	

	

	return render_template("index.html",cantidad_auto=cantidad_auto,cantidad_clientes = cantidad_clientes,granchoque=granchoque)


@app.route('/ELIMINAR',methods=['GET', 'POST'])
def borrar():
	return render_template("eliminar_inicio.html",nombre="nombre")


@app.route('/ELIMINAR_AUTO',methods=['GET', 'POST'])
def borrarauto():
	if request.method == 'POST':
		patente =  request.form['PATENTE']
		sql= """delete from mediciones where mediciones.patente='%s';"""%(patente)
		sql2= """delete from autos where autos.patente ='%s';""" %(patente)
		print sql, ' \n' , slq2
		try:
			print(sql)
			print(cur.execute(sql))
			conn.commit()
			print(cur.execute(sql2))
			print(sql2)
			conn.commit()
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
		sql= """ delete from clientes where clientes.rut = '%s'"""%(rutcliente)
		sql2= """ delete from autos where autos.rut = '%s'"""%(rutcliente)
		print sql, '\n', sql2
		try:
			print("sql lo intenta")
			x=cur.execute(sql)
			conn.commit()
			print(x)
			if x is None:
				print("sql falla")
				return render_template("eliminar_error.html",nombre="nombre")
			
			print(cur.execute(sql2))
			conn.commit()
			return render_template("eliminacion_ok.html",nombre="nombre")
		except:
			return render_template("eliminar_error.html",nombre="nombre")
	else:
		return render_template("eliminar_cliente.html",nombre="nombre")


@app.route('/ELIMINAR_DEBE',methods=['GET', 'POST'])
def eliminardebe():
	if request.method == 'POST':
		iddebe = request.form['ID']
		rutdebe = request.form['RUT']
		sql= """delete from debe where debe.id_penalizacion ='%s' AND debe.rut='%s'"""%(iddebe,rutdebe)
		print sql,'\n'
		try:
			
			cur.execute(sql)
			conn.commit
			return render_template("eliminacion_ok.html",nombre="nombre")
		except:
			return render_template("eliminar_error.html",nombre="nombre")
	else:
		return render_template("eliminar_multa.html",nombre="nombre")


@app.route('/ACTUALIZAR', methods=['GET','POST'])
def actualizar():
	return render_template('actualizar_inicio.html')

@app.route('/ACTUALIZAR_DUENO',methods=['GET','POST'])
def actualizardueno():
	if request.method == 'POST':
		try:
			print 'intentado borrar la wea'
			rutdueno = request.form['RUT']
			patente2 = request.form['PATENTE']
			sql= """select * from autos where autos.patente = '%s' for update;"""%(patente2)
			sql2="""update autos set rut='%s' where autos.patente = '%s';"""%(rutdueno, patente2)
			print sql , '\n' , sql2
			cur.execute(sql)
			conn.commit()
			data=cur.fetchall()
			if data:
				print data
				print 'intentando denuevo ctm'
				try:
					
					cur.execute(sql2)
					conn.commit()
					data=cur.fetchall()
					print data
					return render_template("actualizar_exito.html",nombre="nombre")
				except:		
					return render_template("error_actualizar_dueno.html",nombre="nombre")
		except:
			return render_template("actualizar_error.html",nombre="nombre")
	else:
		return render_template("actualizar_dueno.html",nombre="nombre")


@app.route('/ACTUALIZAR_FECHADEBE',methods=['GET','POST'])
def actualizardebe():
	if request.method == 'POST':
		ruta = request.form['RUT']
		fecha = request.form['FECHA_NUEVA']
		id = request.form['IDMULTA']
		sql= """select * from debe where debe.rut='%s' and debe.id_penalizacion=%s for update;"""%(ruta, id)
		sql2="""update debe set fecha_vencimiento='%s' where debe.rut='%s' and debe.id_penalizacion=%s;"""%(fecha,ruta, id)
		print sql, '\n' ,sql2
		try:
			print 'intentado subir'
			print cur.execute(sql)
			conn.commit()
			data= cur.fetchall()
			print data
			print cur.execute(sql2)
			conn.commit()
			return render_template("actualizar_exito.html",nombre="nombre")
		except:
			return render_template("actualizar_error.html",nombre="nombre")
	else:
		return render_template("actualizar_fecha_debe.html",nombre="nombre")	

@app.route('/ACTUALIZAR_TELEFONO',methods=['GET','POST'])
def actualizartelefono():
	if request.method == 'POST':
		ruttel = request.form['RUT']
		telefono = request.form['TELEFONO']
		sql= """select * from clientes where clientes.rut = '%s' for update;"""%(ruttel)
		sql2= """update clientes set telefono='%s' where clientes.rut = '%s';"""%(telefono, ruttel)
		print sql, '\n', sql2
		try:
			print 'intentando subir'
			print cur.execute(sql)
			conn.commit()
			data= cur.fetchall()
			print data
			print cur.execute(sql2)
			conn.commit()
			data= cur.fetchall()
			print data
			return render_template("actualizar_exito.html",nombre="nombre")
		except:
			return render_template("actualizar_error.html",nombre="nombre")
	else:
		return render_template("actulizar_telefono_dueno.html",nombre="nombre")	



@app.route('/CREAR_AUTO',methods=['GET','POST'])
def crearauto():
	if request.method == 'POST':
		patentec = request.form['PATENTE']
		rutc = request.form['RUT']
		largoc = request.form['LARGO']
		anchoc = request.form['ANCHO']
		altoc = request.form['ALTO']
		peso_neto = request.form['PESO_NETO']
		combustible = request.form['TIPO_COMBUSTIBLE']
		tipo_auto = request.form['TIPO_AUTO']
		pasajeros = request.form['MAXIMO_PASAJEROS']
		aro = request.form['NUM_ARO']
		try:
			sql = """insert into autos values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """%(patentec,rutc,largoc,anchoc,altoc,peso_neto,combustible,tipo_auto,pasajeros,aro)
			cur.execute(sql)
			conn.commit()
			return render_template("crear_ok.html", nombre="nombre")
		except:
			return render_template("crear_error.html",nombre="nombre")
	else:
		return render_template("crear_auto.html",nombre="nombre")

@app.route('/CREAR_CLIENTE',methods=['GET','POST'])
def crearcliente():
	if request.method == 'POST':
		rutd = request.form['RUT']
		digito = request.form['DIGITO']
		nombred = request.form['NOMBRE']
		apellidod = request.form['APELLIDO']
		email = request.form['EMAIL']
		telefonod = request.form['TELEFONO']
		url = request.form['URL']
		try:
			sql = """insert into clientes values(%s,%s,%s,%s,%s,%s,%s) """%(rutd,digito,nombred,apellidod,email,telefonod,url)
			cur.execute(sql)
			conn.commit()
			return render_template("crear_exito.html", nombre="nombre")
		except:
			return render_template("crear_error.html",nombre="nombre")
	else:
		return render_template("crear_cliente.html",nombre="nombre")

@app.route('/REVISAR',methods=['GET','POST'])
def revisar():
	return render_template("revisar_inicio.html")

@app.route('/REVISAR_FALTAS',methods=['GET','POST'])
def revisarfaltas():
	if request.method == 'POST':
		rutr = request.form['rut']
		try:
			sql = """select faltas.monto from clientes, debe, faltas where clientes.rut = %s AND clientes.rut = debe.rut AND debe.id_penalizacion=faltas.id_penalizacion;"""
			cur.execute(sql)
			conn.commit()
			return render_template("revisar_exito.html",nombre="nombre")
		except:
			return render_template("revisar_fallo.html",nombre="nombre")
	else:
		return render_template("revisar_faltas.html",nombre="nombre")

@app.route('/REVISAR_CHOQUEMAYOR',methods=['GET','POST'])
def revisarmayorchoque():
	
		
	sql = """select choques.calle, choques.numeracion, choques.fecha, choques.hora from choques,
	(select count(*) as cantidad, id_evento from involucrados group by id_evento
	) as kk where kk.cantidad  = (select max(cosas) from (select count(*) as cosas 
	from involucrados group by id_evento) as jj) and choques.id_evento = kk.id_evento;"""

	cur.execute(sql)
	print sql
	granchoque = cur.fetchall
	
	conn.commit()
		
	
	return render_template("revisar_choquemayor.html",granchoque = granchoque)

@app.route('/REVISAR_MEDICIONES',methods=['GET','POST'])
def revisarubicacionesgps():
	if request.method == 'POST':
		patente = request.form['PATENTE']
		sensor_id = request.form['SENSOR_ID']
		fecha_medicion = request.form['FECHA']
		try:
			sql = """SELECT mediciones.patente, mediciones.hora FROM mediciones where mediciones.patente=%s  and mediciones.id_sensor =%s and mediciones.fecha = %s ORDER BY mediciones.hora;"""%(patente, sensor_id, fecha_medicion)
			cur.execute(sql)
			conn.commit()
			return render_template("revisar_exito.html",nombre="nombre")
		except:
			return render_template("revisar_fallo.html",nombre="nombre")
	else:
		return render_template("revisar_ubicacionesgps.html",nombre="nombre")


@app.route('/tablas')
def tablas():
	return render_template("tables.html",nombre="nombre")
