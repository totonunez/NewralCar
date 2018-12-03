import csv 

santiago = []
concepcion = []
valparaiso = []
serena = []
antofagasta = []
temuco = []
rancagua = []
iquique = []
talca = []
arica = []
puertomontt = []
chillan = []
angeles = []
calama = []
copiapo = []
osorno = []
quillota = []
valdivia = []
puntaarenas = []
sanantonio = []
curico = []
ovalle = []
linares = []
andes = []
melipilla = []
sanfelipe = []


with open('Ciudades.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        santiago.append(row['Gran Santiago'])
        concepcion.append(row['Gran Concepcion'])
        valparaiso.append(row['Gran Valparaiso'])
        serena.append(row['Gran La Serena'])
        antofagasta.append(row['Antofagasta'])
        temuco.append(row['Gran Temuco'])
        rancagua.append(row['Gran Rancagua'])
        iquique.append(row['Gran Iquique'])
        talca.append(row['Talca'])
        arica.append(row['Arica'])
        puertomontt.append(row['Gran Puerto Montt'])
        chillan.append(row['Gran Chillan'])
        angeles.append(row['Los Angeles'])
        calama.append(row['Calama'])
        copiapo.append(row['Copiapo'])
        osorno.append(row['Osorno'])
        quillota.append(row['Gran Quillota'])
        valdivia.append(row['Valdivia'])
        puntaarenas.append(row['Punta Arenas'])
        sanantonio.append(row['Gran San Antonio'])
        curico.append(row['Curico'])
        ovalle.append(row['Ovalle'])
        linares.append(row['Linares'])
        andes.append(row['Los Andes'])
        melipilla.append(row['Melipilla'])
        sanfelipe.append(row['San Felipe'])


print(santiago)