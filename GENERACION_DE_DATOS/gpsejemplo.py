connectionRegistry = QgsGPSConnectionRegistry().instance()

# Ahora listamos las conexiones disponible en el registro

connectionList = connectionRegistry.connectionList()

# Si sólo tenemos una, cogemos la información de la primera:

GPSInfo = connectionList[0].currentGPSInformation()

# Y ahora extraemos la información que nos interese

longitude = GPSInfo.longitude
latitude = GPSInfo.latitude