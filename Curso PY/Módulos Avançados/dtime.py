import datetime

t = datetime.time(4, 20, 1) #horas, minutos, segundos

# print(t)

today = datetime.date(2023, 1, 13)

# print(today.day)
# print(today.year)
# print(today.month)

dt = datetime.datetime(2022, 1, 13, 15, 18, 45)

# print(dt)

dt = dt.replace(2023)

# print(dt)

# DATE -----

from datetime import date

date1 = date(2023,4,1)
date2 = date(2023,1,13)

#print(date1-date2)

dt1 = datetime.datetime(2023,4,1, 22, 50, 00)
dt2 = datetime.datetime(2023,1,13,15,18,45)

#print(dt1-dt2)

# CURRENT DATETIME -----

from datetime import datetime

current_time = datetime.now()
missing_time = str(dt1 - current_time)
print("Tempo faltando =", missing_time[0:16])