# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 13:21:04 2021

@author: juanr
"""
import requests
import json

api_url = "https://startup.bolsadesantiago.com/api/consulta/ClienteMD/getInstrumentosRV?access_token=FF8BA3AFBEA440B588CB0CF3B77BE856"
response =requests.post(api_url)

datJson=response.json()


datJson1=json.dumps(datJson, indent=4, sort_keys=True)
# datJson2=json.load(response.json())

print(json.dumps(datJson, indent=4, sort_keys=True))

# print(datJson2['codTicker'])

print("************************************************")
for t in json.dumps(datJson, indent=4, sort_keys=True):
    print(t)
print("************************************************")

# print(datJson)
print(datJson1)


with open("c:\paso\sample.json", "w") as outfile: 
    json.dump(datJson1, outfile)
    
    

with open("c:\paso\sample.json", "r") as JSON:
       json_dict = json.load(JSON)
       print(json_dict["instruments"])

# print(response.text)

# for t in response:
#     u=len(t)
#     for tt in range(0,u):        
#           print( "Dato \t", t[tt], "  Posicion \t", tt)
# print()
# print(response.json())
# print(response.status_code)