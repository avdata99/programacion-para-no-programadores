from datetime import date, datetime, timedelta


hoy = date.today()
print(hoy)
# 2022-02-12
print(type(hoy))
# <class 'datetime.date'>

manana = hoy + timedelta(days=1)
print(manana)
# 2022-02-13

ahora = datetime.now()
print(ahora)
# 2022-02-12 14:35:16.687589

print(type(ahora))
# <class 'datetime.datetime'>

en_15 = ahora + timedelta(minutes=15)
print(en_15)
# 2022-02-12 14:50:16.687589

hoy = date.today()
print(hoy.strftime("%d/%m/%Y"))
# 12/02/2022

print(hoy.strftime("%d de %B de %Y"))
# 12 de February de 2022
