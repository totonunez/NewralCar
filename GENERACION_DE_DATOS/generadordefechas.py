from datetime import datetime, timedelta, date, time
from random import choice, random

inicio = datetime(2010,1,1)
fin    = datetime(2018,11,16)
lista_fechas = [(inicio + timedelta(days=d)).strftime("%Y-%m-%d")
                    for d in range((fin - inicio).days + 1)] 
print(choice(lista_fechas))