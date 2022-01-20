import json
import os
import requests


data_file = 'cba.json'

# si no existe el archivo, lo bajo
if not os.path.isfile(data_file):
    url = 'https://transparencia.cba.gov.ar/HandlerMasterConsulta.ashx?anio=201&Mes=0&Prove=prov&_search=false&nd=1642649153273&rows=10&page=1&sidx=invdate&sord=desc'
    response = requests.get(url, timeout=360)

    f = open(data_file, 'w')
    f.write(response.text)
    f.close()

data = json.load(open(data_file))

for proveedor in data:
    print(f' - proveedor {proveedor["RAZON"]}')
    # values = [
    #     (key, value)
    #     for key, value in proveedor.items()
    #     if key not in ['RAZON', 'id_proveedor'] and value is not None]
    # if len(values) > 0:
    #     raise Exception(values)

print(f'Total proveedores: {len(data)}')


""" ejemplo de un registro

{
	"nro_nombre_jurisdiccion":null,
	"nro_nombre_unidad_adm":null,
	"prog":null,
	"subprog":null,
	"numero_objeto":null,
	"parpri":null,
	"parpar":null,
	"parsub":null,
	"pardet":null,
	"nro_nombre_fuente_fin":null,
	"finalidad":null,
	"final_sin_num":null,
	"funcion":null,
	"credito_original":null,
	"compensaciones_p":null,
	"compensaciones_n":null,
	"ajustes":null,
	"credito_vgte":null,
	"compromiso_preventivo":null,
	"credito_disponible":null,
	"compromiso_definitivo":null,
	"devengado":null,
	"ordenado_a_pagar":null,
	"pagado":null,
	"id_jurisdiccion":null,
	"id_unidad_adm":null,
	"id_cat_prog":null,
	"id_vigencia":null,
	"id_objeto_gasto":null,
	"id_fuente_fin":null,
	"id_funcion":null,
	"fecha":null,
	"ejercicio":null,
	"nombre_funcion":null,
	"id_funcion_rel":null,
	"id_nivel":null,
	"numero_funcion":null,
	"economico_gasto":null,
	"personalyrel":null,
	"fecha_actualizacion":null,
	"preventivo_npmp":null,
	"preventivo_oc":null,
	"importe_def_oc":null,
	"importe_def_dev":null,
	"id_eco_gasto":null,
	"NRO_DEVENGADO":null,
	"NRO_COMPROBANTE":null,
	"FECHA_ORDENADOPAGAR":null,
	"ID_DEVENGADO":null,
	"IMPORTEDEV":null,
	"N_ITEM":null,
	"NOMBRECAT":null,
	"NOMBRE_OBJETO":null,
	"CENTROCOSTO":null,
	"IMPORTEDEVDET":null,
	"CANTIDAD":null,
	"NOMBRECATPADRE":null,
	"NOMBRECATHIJO":null,
	"CODIGOPADRECAT":null,
	"CODIGOHIJOCAT":null,
	"id_cat_prog_rel":null,
	"id_objeto_rel":null,
	"IMPUTA_FORMU":null,
	"RAZON":"VILLANUEVA PABLO ANDRES",
	"id_proveedor":31325551,
	"latitud":null,
	"longitud":null,
	"nobras":null,
	"id_estadoObras":null,
	"nombreComuna":null,
	"nombreMunicipio":null,
	"partida":null,
	"id_Obra":null,
	"codigo":null,
	"id_item":null
}

"""