import csv
def read_csv(filepath):
    table = list()  # Tabela é uma lista de linhas
    with open(filepath) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            table.append(row)

    return table

titanic_tbl = read_csv("train.csv")

def is_float(x):
  try:
    float(x)
    return True
  except:
    return False

idades = [float(passg["Age"]) for passg in titanic_tbl
               if is_float(passg["Age"])]
idades_vivos = [float(passg["Age"]) for passg in titanic_tbl
               if is_float(passg["Age"]) and passg["Survived"] == "1"]
idades_mortos = [float(passg["Age"]) for passg in titanic_tbl
                if is_float(passg["Age"]) and passg["Survived"] == "0"]

media = sum(idades) / len(idades)
media_vivos = sum(idades_vivos) / len(idades_vivos)
media_mortos = sum(idades_mortos) / len(idades_mortos)

print("Média idade todos:", "%.1f" % media)
print("Média idade vivos:", "%.1f" % media_vivos)
print("Média idade mortos:", "%.1f" % media_mortos)
