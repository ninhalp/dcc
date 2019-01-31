import csv

def read_csv(filepath):
    table = list()  # Tabela é uma lista de linhas
    with open(filepath) as csv_file:
        reader = csv.DictReader('train.csv')
        for row in reader:
            table.append(row)
            media_age = row['Age']/2
    
    return table and media_age



    
