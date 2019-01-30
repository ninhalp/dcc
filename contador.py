import requests
import json

lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)
print(lista)

#conj = set(lista)
dicionario = {}
#dicionario[x] = dict(lista)

for x in lista:
  if x in dicionario:
    dicionario[x] += 1
  else:
    dicionario[x] = 1

print(dicionario)
