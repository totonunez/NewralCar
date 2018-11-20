import random
from datetime import datetime, timedelta

inicio = datetime(2017, 1, 30)
final =  datetime(2017, 5, 28)


random_date = inicio + timedelta(seconds= int((final - inicio).total_seconds() * random.random()))

print(random_date)
print(str(inicio))
print(type(inicio))