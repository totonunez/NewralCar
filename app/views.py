from app import app
from flask import render_template,request,redirect
from configuraciones import *
import psql_pruebas as P
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

		
	except:
		pass
	

	

	return render_template("index.html",cantidad_auto=cantidad_auto,cantidad_clientes = cantidad_clientes)


@app.route('/ELIMINAR',methods=['GET', 'POST'])
def borrar():
	return render_template("eliminar_inicio.html")


@app.route('/ELIMINAR_AUTO',methods=['GET', 'POST'])
def borrarauto():
	if request.method == 'POST':
		patente =  request.form['PATENTE']
        	if P.ELIMINAR_AUTO(patente):
            		return render_template("eliminacion_ok.html")
        	else:
            		return render_template("eliminar_error.html")			
	else:
		return render_template("eliminar_auto.html")



@app.route('/ELIMINAR_CLIENTE',methods=['GET', 'POST'])
def borrarcliente():
	if request.method == 'POST':
		rutcliente = request.form['RUT']
        	status=P.ELIMINAR_CLIENTE(rutcliente)
        	if status:
            		return render_template("eliminacion_ok.html")
        	else:
            		return render_template("eliminar_error.html")
	else:
		return render_template("eliminar_cliente.html")


@app.route('/ELIMINAR_DEBE',methods=['GET', 'POST'])
def eliminardebe():
	if request.method == 'POST':
		iddebe = request.form['IDMULTA']
		rutdebe = request.form['RUT']
        	if P.ELIMINAR_MULTA(rutdebe, iddebe):
            		return render_template("eliminacion_ok.html")
        	else:
            		return render_template("eliminar_error.html")
	else:
		return render_template("eliminar_multa.html")


@app.route('/ACTUALIZAR', methods=['GET','POST'])
def actualizar():
	return render_template('actualizar_inicio.html')

@app.route('/ACTUALIZAR_DUENO',methods=['GET','POST'])
def actualizardueno():
	if request.method == 'POST':
		rutdueno = request.form['RUT']
		patente2 = request.form['PATENTE']
            	status=P.ACTUALIZAR_DUENO(rutdueno,patente2)
            	if status:
                	return render_template("actualizar_exito.html")
            	else:
                	if status is None:
                    		return render_template("actualizar_error.html")
                	else:
                    		return render_template("error_actualizar_dueno.html")
	else:
		return render_template("actualizar_dueno.html")


@app.route('/ACTUALIZAR_FECHADEBE',methods=['GET','POST'])
def actualizardebe():
	if request.method == 'POST':
		ruta = request.form['RUT']
		fecha = request.form['FECHA_NUEVA']
		id = request.form['IDMULTA']
        	if P.ACTUALIZAR_FECHA_DEBE(ruta,fecha,id):
            		return render_template("actualizar_exito.html")
        	else:
            		return render_template("actualizar_error.html")
	else:
		return render_template("actualizar_fecha_debe.html")	

@app.route('/ACTUALIZAR_TELEFONO',methods=['GET','POST'])
def actualizartelefono():
	if request.method == 'POST':
		ruttel = request.form['RUT']
		telefono = request.form['TELEFONO']
        	if P.ACTUALIZAR_TELEFONO(ruttel, telefono):
            		return render_template("actualizar_exito.html")
        	else:
            		return render_template("actualizar_error.html")
	else:
		return render_template("actulizar_telefono_dueno.html")	



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
		pasajeros = request.form['MAXIMO_PASAJERO']
		aro = request.form['NUM_ARO']
        	if P.INGRESAR_AUTO_NUEVO(patentec,rutc,largoc,anchoc,altoc,peso_neto,combustible,tipo_auto,pasajeros,aro):
            		return render_template("crear_exito.html", nombre="nombre")
        	else:
            		return render_template("crear_error.html")
	else:
		return render_template("crear_auto.html")

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
        	if P.INGRESAR_CLIENTE_NUEVO(rutd,digito,nombred,apellidod,email,telefonod,url):
            		return render_template("crear_exito.html", nombre="nombre")
        	else:
            		return render_template("crear_error.html")
	else:
		return render_template("crear_cliente.html")

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
			return render_template("revisar_exito.html")
		except:
			return render_template("revisar_fallo.html")
	else:
		return render_template("revisar_faltas.html")

@app.route('/REVISAR_GPS',methods=['GET','POST'])
def GPS():
    if request.method=='POST':
        patente = request.form['PATENTE']
        clave=request.form['PASS']
	print clave
        if clave == 'HOLAMUNDO':
		print 'true'
		try:
			data=P.CONSULTAS_GPS(patente)
			if data:
				return render_template("gps_tablas.html",data=data)
			else:
				return render_template("gps_error.html")
		except:
			return render_template("gps_error.html")	
        else:
            return render_template("gps_error.html")
    else:
        return render_template("gps_inicio.html")


@app.route('/REVISAR_MEDICIONES',methods=['GET','POST'])
def verisarubicacion():
	if request.method == 'POST':
		patente = request.form['PATENTE']
		id = request.form['ID']
		l,TYPE_SENSOR=P.CONSULTAS_MEDICIONES(patente,id)
		t=len(l)
		first='[{y:'
		medio='}, {y:'
		end='}]'
		data=first
		for i in range(t):
			if i is 39:
				data=data+str(l[i][1])
			else:
				data=data+str(l[i][1])+medio
		data=data+end
		print data
		try:
			return render_template("revisar_exito.html",data=data,TYPE_SENSOR=TYPE_SENSOR)
		except:
			return render_template("revisar_fallo.html")
	else:
		#return render_template("revisar_exito.html")
		return render_template("visualisar_mediciones.html")


@app.route('/tablas')
def tablas():
	return render_template("tables.html")
