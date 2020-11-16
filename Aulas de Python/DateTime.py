# Agora vamos lidar com o tempo!
from datetime import datetime

t = datetime.now()
print(t)
print(t.hour)
print(t.minute)
print(t.second)

today = datetime.today()
print(today)

print(today.ctime())
print(today.year)

# É possível fazer operações aritméticas

d1 = datetime(2015,3,11)
d2 = datetime(2015,8,17)

print(d2-d1)

# Funções importante segundo o professor - Converter datetime pra string e string pra datetime
str_date = d1.strftime('%Y/%m/%d')
print(str_date)