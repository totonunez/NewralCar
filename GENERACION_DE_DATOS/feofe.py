import random
from datetime import datetime

inicio = datetime(2017, 1, 30)
final =  datetime(2017, 5, 28)

random_date = inicio + (final - inicio) * random.random()

print(random_date)