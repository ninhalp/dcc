import json

with open("pessoas.json") as arq:
    pessoas = json.load(arq) #ERROR

print(pessoas)
