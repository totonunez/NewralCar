from configuraciones import *
import psycopg2
conn=psycopg2.connect("dbname=%s user=%s password=%s"%(database, user, passwd))
cur=conn.cursor()
import time


RUT='19233498','10233198','14081177'

def ELIMINAR_CLIENTE(RUT):
    RUT=str(RUT)
    SQL=""" SELECT patente
            FROM autos 
            WHERE autos.rut='%s';"""%(RUT)
    print SQL
    cur.execute(SQL)
    PATENTE=cur.fetchone()
    print 'SE ELIMINARAN LOS ELEMENTOS DE LA PATENTE: ', PATENTE 
    SQL2=""" DELETE FROM involucrados
             WHERE involucrados.patente='%s';"""%(PATENTE)
    print SQL2
    SQL3=""" DELETE FROM mediciones
             WHERE mediciones.patente='%s';"""%(PATENTE)
    print SQL3
    SQL4=""" DELETE FROM autos
             WHERE autos.patente='%s';"""%(PATENTE)
    print SQL4
    SQL5=""" DELETE FROM debe
             WHERE debe.rut='%s';"""%(RUT)
    print SQL5
    SQL6=""" DELETE FROM clientes
             WHERE clientes.rut='%s';"""%(RUT)
    print SQL6
    if PATENTE:
        #try:
        print cur.execute(SQL2)
        DATA_BORRADO_INVOLUCRADOS=cur.fetchone()
        print 'CANTIDAD DE ACCIDENTES ELIMINADOS: ', DATA_BORRADO_INVOLUCRADOS
        print cur.execute(SQL3)
        DATA_BORRADO_MEDICIONES=cur.fetchone()
        print 'CANTIDAD DE MEDICIONES ELIMINADAS: ', DATA_BORRADO_MEDICIONES
        print cur.execute(SQL4)
        DATA_BORRADO_AUTO=cur.fetchone()
        print 'CANTIDAD DE AUTOS ELIMINADOS: ', DATA_BORRADO_AUTO
        print cur.execute(SQL5)
        DATA_BORRADO_DEBE=cur.fetchone()
        print 'CANTIDAD DE MULTAS ELIMINADAS: ', DATA_BORRADO_DEBE
        print cur.execute(SQL6)
        DATA_BORRADO_CLIENTES=cur.fetchone()
        print 'CANTIDAD DE CLIENTES ELIMINADOS: ', DATA_BORRADO_CLIENTES
        #except:
         #   print 'ERROR EN EL INTENTO DE ELIMINAR EN INVOLUCRADOS, MEDICIONES, AUTOS, CLIENTES'
    else:

        print 'ERROR CLIENTE NO TIENE PATENTE ASIGNADA' 

def ELIMINAR_AUTO(PATENTE):
    SQL2=""" DELETE FROM involucrados
             WHERE involucrados.patente='%s';"""%(PATENTE)
    print SQL2
    SQL3=""" DELETE FROM mediciones
             WHERE mediciones.patente='%s';"""%(PATENTE)
    print SQL3
    SQL4=""" DELETE FROM autos
             WHERE autos.patente='%s';"""%(PATENTE)
    print SQL4
    try:
        cur.execute(SQL2)
        DATA_BORRADO_INVOLUCRADOS=cur.fetchall()
        print 'CANTIDAD DE ACCIDENTES ELIMINADOS: ', DATA_BORRADO_INVOLUCRADOS
        cur.execute(SQL3)
        DATA_BORRADO_MEDICIONES=cur.fetchall()
        print 'CANTIDAD DE MEDICIONES ELIMINADAS: ', DATA_BORRADO_MEDICIONES
        cur.execute(SQL4)
        DATA_BORRADO_AUTO=cur.fetchall()
        print 'CANTIDAD DE AUTOS ELIMINADOS: ', DATA_BORRADO_AUTO 
    except:
        print 'ERROR EN EL INTENTO DE ELIMINAR EN INVOLUCRADOS, MEDICIONES, AUTOS, CLIENTES'

def ELIMINAR_MULTA(RUT):
    SQL5=""" DELETE FROM debe
             WHERE debe.rut='%s';"""%(RUT)
    print SQL5
    try:
        cur.execute(SQL5)
        DATA_BORRADO_DEBE=cur.fetchall()
        print 'CANTIDAD DE MULTAS ELIMINADAS: ', DATA_BORRADO_DEBE
    except:
        print 'ERROR EN BORRADO DE MULTAS, RUT INCORRECTO'

def ACTUALIZAR_DUENO(RUT, PATENTE):
    SQL=""" SELECT * 
            FROM autos
            WHERE autos.patente='%s'
            FOR UPDATE;"""%(PATENTE)
    print SQL

    SQL2="""UPDATE autos
            SET rut='%s'
            WHERE autos.patente='%s';"""%(RUT, PATENTE)
    print SQL2
    cur.execute(SQL)
    DATA_PATENTE_RUT=cur.fetchall()
    if DATA_PATENTE_RUT:
        print DATA_PATENTE_RUT
        try:
            cur.execute(SQL2)
            DATA_ACTUALIZACION_DE_DUENO_AUTO=cur.fetchall()
            print 'SE ACTUALIZAN LA SIGUIENTE CANTIDAD DE ELEMENTOS: ',DATA_ACTUALIZACION_DE_DUENO_AUTO
        except:
            print 'ERROR EN EL INTENTO DE ACTUALIZAR, POSIBLEMENTE EL RUT NUEVO NO EXISTE EN EL SISTEMA'
    else:
        print 'NO EXISTE AUTO CON TAL PATENTE'

def ACTUALIZAR_FECHA_DEBE(RUT, FECHA_NUEVA, ID_MULTA):
    SQL=""" SELECT *
            FROM debe
            WHERE debe.rut='%s'
            AND debe.id_penalizacion='%s'
            FOR UPDATE;"""%(RUT, ID_MULTA)
    print SQL
    SQL2="""UPDATE debe
            SET fecha_vencimiento='%s'
            WHERE debe.rut='%s'
            AND debe.id_penalizacion=%s;"""%(FECHA_NUEVA, RUT,ID_MULTA)
    print SQL2
    cur.execute(SQL)
    DATA_CLIENTE_MULTA=cur.fetchall()
    print DATA_CLIENTE_MULTA
    if DATA_CLIENTE_MULTA:
        try:
            cur.execute(SQL2)
            DATA_MULTA_UPDATE=cur.fetchall()
            print 'SE ACTUALIZAN LA SIGUIENTE CANTIDAD DE ELEMENTOS: ',DATA_MULTA_UPDATE
        except:
            print 'ERROR EN EL INTENTO DE ACTUALIZAR FECHAS DE MULTAS'
    else:
        print 'EL RUT INDICADO NO POSEE MULTA DE ID_MULTA ESPECIFICADO'

def ACTUALIZAR_TELEFONO(RUT, TELEFONO):
    SQL=""" SELECT *
            FROM clientes
            WHERE clientes.rut='%s'
            FOR UPDATE;"""%(RUT)
    print SQL
    SQL2="""UPDATE clientes
            SET telefono='%s'
            WHERE clientes.rut='%s';"""%(TELEFONO,RUT)
    print SQL2
    cur.execute(SQL)
    DATA_TELEFONO_CLIENTE=cur.fetchall()
    if DATA_TELEFONO_CLIENTE:
        print DATA_TELEFONO_CLIENTE
        try:
            cur.execute(SQL2)
            DATA_TELEFONO_UPDATE=cur.fetchall()
            print 'SE ACTUALIZAR LA SIGUIENTE CANTIDAD DE TELEFONOS: ', DATA_TELEFONO_UPDATE
        except:
            print 'ERROR EN EL INTENTO DE ACTUALIZAR EL TELEFONO'
    else:
        print 'ERROR EL CLIENTE NO EXISTE O FUE MAL ESCRITO EL RUT'

def INGRESAR_AUTO_NUEVO(PATENTE, RUT, LARGO , ANCHO, ALTO, PESO_NETO, TIPO_COMBUSTIBLE, TIPO_AUTO, MAXIMO_PASAJEROS, NUM_ARO):
    SQL=""" INSERT INTO autos
            (patente, rut, largo, ancho, altos, peso_neto, tipo_combustible, tipo_auto, maximo_pasajeros, num_aro)
            VALUES ('%s', '%s', %s, %s, %s, %s, %s, '%s', '%s',%s, %s);"""%(PATENTE, RUT, LARGO , ANCHO, ALTO, PESO_NETO, TIPO_COMBUSTIBLE, TIPO_AUTO, MAXIMO_PASAJEROS, NUM_ARO)
    print  SQL
    try:
        cur.execute(SQL)
        DATA_AUTO_NUEVO=cur.fetchall()
        print 'SE INGRESO CORRECTAMENTE EL AUTO NUEVO', DATA_AUTO_NUEVO
        SQL_PRUEBA="""SELECT *
                      FROM autos
                      WHERE autos.patente='%s';"""%(PATENTE)
        cur.execute(SQL_PRUEBA)
        DATA_COMPROBACION_AUTO_NUEVO=cur.fetchall()
        print 'COMPROBACION DE ENTRADA: ', DATA_COMPROBACION_AUTO_NUEVO
    except:
        print 'ERROR EN EL INGRESO DE UN AUTO NUEVO'

def INGRESAR_CLIENTE_NUEVO(RUT, DIGITO, NOMBRE, APELLIDO, EMAIL, TELEFONO, URL):
    SQL="""INSERT INTO clientes
           (rut, digito, nombre, apellido , email, telefono, url) 
           VALUES '%s','%s','%s','%s','%s','%s','%s';"""%(RUT, DIGITO, NOMBRE, APELLIDO, EMAIL, TELEFONO, URL)
    print SQL
    try:
        cur.execute(SQL)
        DATA_CLIENTE_NUEVO=cur.fetchall()
        print 'SE INGRESO UN CLIENTE NUEVO', DATA_CLIENTE_NUEVO
        SQL_PRUEBA="""SELECT * 
                      FROM clientes
                      WHERE clientes.rut='%s';"""%(RUT)
        cur.execute(SQL_PRUEBA)
        DATA_COMPROBACION_CLIENTE_NUEVO=cur.fetchall()
        print 'COMPROBACION DE ENTRADA: ', DATA_COMPROBACION_CLIENTE_NUEVO
    except:
        print 'ERROR EN EL INGRESO DE UN CLIENTE NUEVO'
