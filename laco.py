# Laço de Repetição - FOR 0 WHILE

# i=0

# while True:
    # i=i+1
    # print(f"Alessandra - {i}")

numeros = []

for x in range(7):
    n = int(input("Digite o número: "))
    numeros.append(n)

total = sum(numeros)
print(f"A soma dos números digitados foi {total}")