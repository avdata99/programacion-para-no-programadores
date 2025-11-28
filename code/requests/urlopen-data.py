# Ejemplo simple de request HTTP GET usando solo builtins (sin 'with')
import csv
from urllib.request import urlopen

productos_csv_url = "https://raw.githubusercontent.com/avdata99/despensa-sierras-chicas/refs/heads/master/Productos.csv"
"""
ID,IdTipoProducto,nProducto,pCosto,pVenta,CodEnvase
1,10,Granadina Cusenier,35,43,Cerveza
2,2,Brahma,"15,2473106384",20,Cerveza
3,2,Andes,"16,4001235962",20,Cerveza
4,2,Budweiser,"17,889705658",22,Cerveza
5,2,Cordoba,"15,8332223892",20,Cerveza
6,2,Heineken,"31,2754993439",38,Cerveza
"""
ventas_csv_url = "https://raw.githubusercontent.com/avdata99/despensa-sierras-chicas/refs/heads/master/Ventas.csv"
"""
ID,IDVenta,Fecha,IDproducto,Cantidad,Precio,Costo
45830,A-0001-00001162,01/07/2007,277,2,3,"2,4100000858"
45831,A-0001-00001162,01/07/2007,71,1,"3,75","3,4600000381"
45832,A-0001-00001162,01/07/2007,814,1,8,"6,5999999046"
45833,A-0001-00001162,01/07/2007,6,2,"3,25","2,7000000477"
45834,A-0001-00001162,01/07/2007,399,1,2,"1,6599999666"
"""
response = urlopen(productos_csv_url)
productos_txt = response.read().decode("utf-8").splitlines()
response.close()
response = urlopen(ventas_csv_url)
ventas_txt = response.read().decode("utf-8").splitlines()
response.close()

productos = {}
reader = csv.DictReader(productos_txt)
for row in reader:
    productos[row["ID"]] = row["nProducto"]

ventas = []
reader = csv.DictReader(ventas_txt)
for row in reader:
    ventas.append(row)