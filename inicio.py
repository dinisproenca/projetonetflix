import csv

with open("data/titles.csv", encoding="utf-8") as f:
    linhas = list(csv.DictReader(f))



falsos = 0
for i in linhas[0]["genres"]:
    if i == "":
        falsos += 1

print(falsos)
vazios = 0
for linha in linhas:
    if linha["genres"] == "":
        vazios += 1
print(vazios)
vazios_texto = 0
vazios_lista = 0
for linha in linhas:
    if linha["genres"] == "":
        vazios_texto += 1
    elif linha["genres"] == "[]":
        vazios_lista += 1
print(vazios_texto, vazios_lista)

dinis