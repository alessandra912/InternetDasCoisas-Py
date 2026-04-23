n = []

for i in range(5):
    notas = float(input(f"Digite a {i+1}º nota: "))

    while notas < 0 or notas > 10:
        print("Nota inválida!")
        notas = float(input(f"Digite uma nota válida... {i+1}º nota: "))

    n.append(notas)
     
media = sum(n) / 5

acimaMedia = 0
abaixoMedia = 0

for notas in n:
    if notas > media:
        acimaMedia += 1
    elif notas < media:
        abaixoMedia += 1

print("\nNotas: ", n)
print(f"Média das notas:  {media:.2f}")
print("Notas acima da média: ", acimaMedia)
print("Notas abaixo da média:", abaixoMedia)