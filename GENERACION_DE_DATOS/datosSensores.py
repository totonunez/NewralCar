from time import time
from faker import Faker
from random import choice, random
fake = Faker()
tiempo = time()

print("SENSORES")
print("insert into choques (id_sensor, nombre, presicion) values")
x=0
while (x<10):
    print("({},'{}','{}'),".format(x,choice(["Sensor De Presion","Sensor De Presion De Sobrealimentacion",
"Sensor De Masa De Aire","Sensor De Alta Presion","Sonda Lambda",
"Sensor De Velocidad De Rotacion","Sensor De Presion del Deposito","Transmision De Posicion Del Pedal",
"Sensor de Angulo","Sensor de Inclinacion","Sensor De Aceleracion",
"Sensor De Ocupacion De Asiento","Sensor de Magnitud De Giro o Viraje","Sensor De Aceleracion transversal",
"Sensor de Inclinacion","Sensor De Vuelco","Sensor De velocidad de giro Ruedas",
"Sensor De lluvia","Sensor Telemetrico"]),"%.2f" %float(random())))
    x = x+1
    
print(")")

final = time()- tiempo
print"Tiempo total en crearse todos los datos es" , final


