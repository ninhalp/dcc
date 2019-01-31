import csv

def read_csv(filepath):
    table = list()  # Tabela é uma lista de linhas
    with open(filepath) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            table.append(row)

    return table

titanic_tbl = read_csv("train.csv")

soma_idades = 0
contados = 0
soma_idades_vivos = 0
soma_idades_mortos = 0
contados_vivos = 0
contados_mortos = 0

for passg in titanic_tbl:
    try:
      soma_idades += float(passg["Age"])
      if passg["Survived"] == "1":
        soma_idades_vivos += float(passg["Age"])
        contados_vivos += 1
      else:
        soma_idades_mortos += float(passg["Age"])
        contados_mortos += 1
      contados += 1
    except(ValueError):
      pass

print(titanic_tbl)
      
media = soma_idades / contados
print("Média total: ", media)

media_vivos = soma_idades_vivos / contados_vivos
print("Média dos vivos: ", media_vivos)

media_mortos = soma_idades_mortos / contados_mortos
print("Média dos mortos: ", media_mortos)
