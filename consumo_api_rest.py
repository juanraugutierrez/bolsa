# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 00:12:23 2021

@author: juanr
"""

import requests  #Importamos la librería requests
import json

print("SOLICITANDO INFORMACION DE INTERNET")
print("espere....") 
# URL = 'https://restcountries.eu/rest/v2/all'
URL ='https://startup.bolsadesantiago.com/api/consulta/InstrumentosDisponibles/getInstrumentosValidos' 
# configuramos la url
# solicitamos la información y guardamos la respuesta en data.
data= requests.get(URL) 
# parsed = json.loads(data)

print(data(data, indent=4, sort_keys=True))


# for element in data: #iteramos sobre data
#     print(element[0]) #Accedemos a sus valores