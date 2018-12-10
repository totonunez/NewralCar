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

	sql ="""
	select count(*) from clientes;
	"""
	print sql 
	cur.execute(sql)
	cantidad_clientes  = cur.fetchall()

	return render_template("index.html",cantidad_auto=cantidad_auto,cantidad_clientes = cantidad_clientes)


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
			sql= """ delete from clientes where clientes.rut = '%s'"""%(rutcliente)
			x=cur.execute(sql)
			print(x)
			if x is None:
				print("sql falla")
				return render_template("eliminar_error.html",nombre="nombre")
			sql= """ delete from autos where autos.rut = '%s'"""%(rutcliente)
			print(cur.execute(sql))
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
		try:
			sql= """delete from debe where debe.id_penalizacion ='%s'"""%(iddebe)
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
		sql= """select * from autos where autos.patente = '%s' for update;"""%(patente2)
		cur.execute(sql)
		data=cur.fetchall()
		if data:
			try:
				sql="""update autos set rut='%s';"""%(rutdueno)
				cur.execute(sql)
				return render_template("actualizar_exito.html",nombre="nombre")
			except:		
				return render_template("error_actualizar_dueno.html",nombre="nombre")	
	else:
		return render_template("actualizar_dueno.html",nombre="nombre")


@app.route('/ACTUALIZAR_FECHADEBE',methods=['GET','POST'])
def actualizardebe():
	if request.method == 'POST':
		ruta = resquest.form['RUT']
		fecha = request.form['FECHA_NUEVA']
		id = request.form['IDMULTA']
		try:
			sql= """select * from debe where debe.rut='%s' and id_penalizacion=%s for update;"""%(ruta, id)
			cur.execute(sql)
			sql="""update debe set fecha_vencimiento='%s' where debe.rut='%s' and debe.id_penalizacion=%s;"""%(fecha,ruta, id)
			cur.execute(sql)
			conn.commit()
			return render_template("actualizar_exito.html",nombre="nombre")
		except:
			return render_template("actualizar_error.html",nombre="nombre")
	else:
		return render_template("actualizar_fecha_debe.html",nombre="nombre")	

@app.route('/ACTUALIZAR_TELEFONO',methods=['GET','POST'])
def actualizartelefono():
	if request.method == 'POST':
		ruttel = resquest.form['RUT']
		telefono = request.form['TELEFONO']
		try:
			sql= """select * from clientes where cliente.rut = '%s' for update;"""%(ruttel)
			cur.execute(sql)
			sql= """update clientes set telefono='%s' where clientes.rut = '%s';"""%(telefono, ruttel)
			conn.commit()
			return render_template("actualizar_exito.html",nombre="nombre")
		except:
			return render_template("actualizar_error.html",nombre="nombre")
	else:
		return render_template("actulizar_telefono_dueno.html",nombre="nombre")	


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
			cur.execute(sql)
			conn.commit()
			return render_template("crear_ok.html",nombre="nombre")
		except:
			return render_template("crear_error.html",nombre="nombre")
	else:
		return render_template("crear_sensor.html",nombre="nombre")

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
			sql = """insert into sensores values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """%(patentec,rutc,largoc,anchoc,altoc,peso_neto,combustible,tipo_auto,pasajeros,aro)
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
			sql = """insert into sensores values(%s,%s,%s,%s,%s,%s,%s) """%(rutd,digito,nombred,apellidod,email,telefonod,url)
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
	if request.method == 'POST':
		try:
			sql = """select choques.calle, choques.numeracion, choques.fecha, choques.hora from choques,(select count(*) as cantidad, id_evento from involucrados group by id_evento) as kk where kk.cantidad  = (select max(cosas) from (select count(*) as cosas from involucrados group by id_evento) as jj) and choques.id_evento = kk.id_evento;"""
			cur.execute(sql)
			conn.commit()
			return render_template("revisar_ok.html",nombre="nombre")
		except:
			return render_template("revisar_fallo.html",nombre="nombre")
	else:
		return render_template("revisar_choquemayor.html",nombre="nombre")

@app.route('/REVISAR_UICACIONESGPS',methods=['GET','POST'])
def revisarubicacionesgps():
	if request.method == 'POST':
		patentegps = request.form['PATENTE']
		try:
			sql = """SELECT mediciones.patente, mediciones.fecha, mediciones.hora, mediciones.latitud , mediciones.longitud FROM mediciones where mediciones.patente=%s GROUP BY  mediciones.hora, mediciones.latitud, mediciones.longitud, mediciones.fecha ,mediciones.patente ORDER BY  mediciones.fecha, mediciones.hora;"""%(patentegps)
			cur.execute(sql)
			conn.commit()
			return render_template("revisar_exito.html",nombre="nombre")
		except:
			return render_template("revisar_fallo.html",nombre="nombre")
	else:
		return render_template("revisar_ubicacionesgps.html",nombre="nombre")

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
