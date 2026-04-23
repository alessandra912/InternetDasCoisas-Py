numeros = []
pares = []
impares = []

for i in range(6):
    n = int(input("\nDigite 6 números inteiros: "))
    numeros.append(n)

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\nLista completa dos números: ", numeros)
print("Números pares: ", pares)
print("Números ímpares: ", impares)