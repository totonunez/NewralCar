from configuraciones import *
import psycopg2
conn=psycopg2.connect("dbname=%s user=%s password=%s"%(database, user, passwd))
cur=conn.cursor()
import time

def ELIMINAR_CLIENTE(RUT):
    RUT=str(RUT)
    SQL=""" SELECT patente
            FROM autos 
            WHERE autos.rut='%s';"""%(RUT)
    print SQL
    cur.execute(SQL)
    PATENTE=cur.fetchone()
    conn.commit()
    print 'SE ELIMINARAN LOS ELEMENTOS DE LA PATENTE: ', PATENTE 
    SQL2=""" DELETE FROM involucrados
             WHERE involucrados.patente='%s' RETURNING *;"""%(PATENTE)
    print SQL2
    SQL3=""" DELETE FROM mediciones
             WHERE mediciones.patente='%s';"""%(PATENTE)
    print SQL3
    SQL4=""" DELETE FROM autos
             WHERE autos.patente='%s' RETURNING *;"""%(PATENTE)
    print SQL4
    SQL5=""" DELETE FROM debe
             WHERE debe.rut='%s' RETURNING *;"""%(RUT)
    print SQL5
    SQL6=""" DELETE FROM clientes
             WHERE clientes.rut='%s' RETURNING *;"""%(RUT)
    print SQL6
    if PATENTE:
        try:
            print cur.execute(SQL2)
            DATA_BORRADO_INVOLUCRADOS=cur.fetchall()
            conn.commit()
            print 'CANTIDAD DE ACCIDENTES ELIMINADOS: ', DATA_BORRADO_INVOLUCRADOS
            print cur.execute(SQL3)
            conn.commit()
            #DATA_BORRADO_MEDICIONES=cur.fetchall()
            #print 'CANTIDAD DE MEDICIONES ELIMINADAS: ', DATA_BORRADO_MEDICIONES
            print cur.execute(SQL4)
            DATA_BORRADO_AUTO=cur.fetchall()
            conn.commit()
            print 'CANTIDAD DE AUTOS ELIMINADOS: ', DATA_BORRADO_AUTO
            print cur.execute(SQL5)
            DATA_BORRADO_DEBE=cur.fetchall()
            conn.commit()
            print 'CANTIDAD DE MULTAS ELIMINADAS: ', DATA_BORRADO_DEBE
            print cur.execute(SQL6)
            DATA_BORRADO_CLIENTES=cur.fetchall()
            conn.commit()
            print 'CANTIDAD DE CLIENTES ELIMINADOS: ', DATA_BORRADO_CLIENTES
            return True
        except:
            print 'ERROR EN EL INTENTO DE ELIMINAR EN INVOLUCRADOS, MEDICIONES, AUTOS, CLIENTES'
            return False
    else:
        print 'ERROR CLIENTE NO TIENE PATENTE ASIGNADA' 
        return False

def ELIMINAR_AUTO(PATENTE):
    SQL2=""" DELETE FROM involucrados
             WHERE involucrados.patente='%s' RETURNING *;"""%(PATENTE)
    print SQL2
    SQL3=""" DELETE FROM mediciones
             WHERE mediciones.patente='%s' RETURNING *;"""%(PATENTE)
    print SQL3
    SQL4=""" DELETE FROM autos
             WHERE autos.patente='%s' RETURNING *;"""%(PATENTE)
    print SQL4
    try:
        cur.execute(SQL2)
        DATA_BORRADO_INVOLUCRADOS=cur.fetchall()
        conn.commit()
        print 'CANTIDAD DE ACCIDENTES ELIMINADOS: ', DATA_BORRADO_INVOLUCRADOS
        cur.execute(SQL3)
        conn.commit()
        #DATA_BORRADO_MEDICIONES=cur.fetchall()
        #print 'CANTIDAD DE MEDICIONES ELIMINADAS: ', DATA_BORRADO_MEDICIONES
        cur.execute(SQL4)
        conn.commit()
        DATA_BORRADO_AUTO=cur.fetchall()
        print 'CANTIDAD DE AUTOS ELIMINADOS: ', DATA_BORRADO_AUTO
        return True
    except:
        print 'ERROR EN EL INTENTO DE ELIMINAR EN INVOLUCRADOS, MEDICIONES, AUTOS, CLIENTES'
        return False

def ELIMINAR_MULTA(RUT, ID):
    SQL5=""" DELETE FROM debe
             WHERE debe.rut='%s'
             AND debe.id_penalizacion=%s
             RETURNING *;"""%(RUT, ID)
    print SQL5
    try:
        cur.execute(SQL5)
        DATA_BORRADO_DEBE=cur.fetchall()
        conn.commit()
        print 'CANTIDAD DE MULTAS ELIMINADAS: ', DATA_BORRADO_DEBE
        return True
    except:
        print 'ERROR EN BORRADO DE MULTAS, RUT INCORRECTO'
        return False

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
    conn.commit()
    if DATA_PATENTE_RUT:
        print DATA_PATENTE_RUT
        try:
            cur.execute(SQL2)
            #DATA_ACTUALIZACION_DE_DUENO_AUTO=cur.fetchall()
            conn.commit()
            print 'SE ACTUALIZAN CORRECTAMENTE LOS ELEMENTOS'#,DATA_ACTUALIZACION_DE_DUENO_AUTO
            return True
        except:
            print 'ERROR EN EL INTENTO DE ACTUALIZAR, POSIBLEMENTE EL RUT NUEVO NO EXISTE EN EL SISTEMA'
            return False
    else:
        print 'NO EXISTE AUTO CON TAL PATENTE'
        return None

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
    conn.commit()
    print DATA_CLIENTE_MULTA
    if DATA_CLIENTE_MULTA:
        try:
            cur.execute(SQL2)
            #DATA_MULTA_UPDATE=cur.fetchall()
            conn.commit()
            print 'SE ACTUALIZAN LA SIGUIENTE CANTIDAD DE ELEMENTOS: '#,DATA_MULTA_UPDATE
            return True
        except:
            print 'ERROR EN EL INTENTO DE ACTUALIZAR FECHAS DE MULTAS'
            return False
    else:
        print 'EL RUT INDICADO NO POSEE MULTA DE ID_MULTA ESPECIFICADO'
        return False

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
    conn.commit()
    if DATA_TELEFONO_CLIENTE:
        print DATA_TELEFONO_CLIENTE
        try:
            cur.execute(SQL2)
            #DATA_TELEFONO_UPDATE=cur.fetchall()
            conn.commit()
            print 'SE ACTUALIZAR LA SIGUIENTE CANTIDAD DE TELEFONOS: '#, DATA_TELEFONO_UPDATE
            return True
        except:
            print 'ERROR EN EL INTENTO DE ACTUALIZAR EL TELEFONO'
            return False
    else:
        print 'ERROR EL CLIENTE NO EXISTE O FUE MAL ESCRITO EL RUT'
        return False

def INGRESAR_AUTO_NUEVO(PATENTE, RUT, LARGO , ANCHO, ALTO, PESO_NETO, TIPO_COMBUSTIBLE, TIPO_AUTO, MAXIMO_PASAJEROS, NUM_ARO):
    SQL=""" INSERT INTO autos
            VALUES ('%s', '%s',' %s', '%s', '%s', '%s', '%s', '%s', '%s','%s');"""%(PATENTE, RUT, LARGO , ANCHO, ALTO, PESO_NETO, TIPO_COMBUSTIBLE, TIPO_AUTO, MAXIMO_PASAJEROS, NUM_ARO)
    print  SQL
    try:
        cur.execute(SQL)
        #DATA_AUTO_NUEVO=cur.fetchall()
        conn.commit()
        #print 'SE INGRESO CORRECTAMENTE EL AUTO NUEVO', DATA_AUTO_NUEVO
        SQL_PRUEBA="""SELECT *
                      FROM autos
                      WHERE autos.patente='%s';"""%(PATENTE)
        print SQL_PRUEBA
        cur.execute(SQL_PRUEBA)
        DATA_COMPROBACION_AUTO_NUEVO=cur.fetchall()
        conn.commit()
        print 'COMPROBACION DE ENTRADA: ', DATA_COMPROBACION_AUTO_NUEVO
        return True
    except:
        print 'ERROR EN EL INGRESO DE UN AUTO NUEVO, DEBE INGRESAR UN RUT QUE EXISTE EN CLIENTES'
        return False

def INGRESAR_CLIENTE_NUEVO(RUT, DIGITO, NOMBRE, APELLIDO, EMAIL, TELEFONO, URL):
    SQL="""INSERT INTO clientes 
           VALUES ('%s','%s','%s','%s','%s','%s','%s');"""%(RUT, DIGITO, NOMBRE, APELLIDO, EMAIL, TELEFONO, URL)
    print SQL
    try:
        cur.execute(SQL)
        #DATA_CLIENTE_NUEVO=cur.fetchall()
        conn.commit()
        #print 'SE INGRESO UN CLIENTE NUEVO', DATA_CLIENTE_NUEVO
        SQL_PRUEBA="""SELECT * 
                      FROM clientes
                      WHERE clientes.rut='%s';"""%(RUT)
        print SQL_PRUEBA
        cur.execute(SQL_PRUEBA)
        DATA_COMPROBACION_CLIENTE_NUEVO=cur.fetchall()
        conn.commit()
        print 'COMPROBACION DE ENTRADA: ', DATA_COMPROBACION_CLIENTE_NUEVO
        return True
    except:
        print 'ERROR EN EL INGRESO DE UN CLIENTE NUEVO'
        return False

def CONSULTAS_GPS(PATENTE):
    SQL="""SELECT mediciones.patente, mediciones.fecha, mediciones.hora, mediciones.latitud , mediciones.longitud
           FROM mediciones
           WHERE mediciones.patente='%s' 
           AND mediciones.fecha=(SELECT max(t2.fecha)
                                 FROM (SELECT mediciones.fecha as fecha 
                                       FROM mediciones
                                       WHERE mediciones.patente='%s') as t2)
           GROUP BY  mediciones.hora, mediciones.latitud, mediciones.longitud, mediciones.fecha ,mediciones.patente
           ORDER BY  mediciones.fecha, mediciones.hora;"""%(PATENTE, PATENTE)
    
    print SQL
    try:
        cur.execute(SQL)
        DATA_GPS_CONFIDENCIAL=cur.fetchall()
        conn.commit()
        print 'GPS OK'
        return DATA_GPS_CONFIDENCIAL
    except:
        return []

def CONSULTAS_MEDICIONES(PATENTE,IDSENSOR, FECHA):
    SQL ="""
    SELECT mediciones.patente, mediciones.hora
    FROM mediciones where mediciones.patente=%s 
    AND mediciones.id_sensor =%s
    AND mediciones.fecha = %s
    ORDER BY mediciones.hora;"""%(PATENTE, IDSENSOR, FECHA)