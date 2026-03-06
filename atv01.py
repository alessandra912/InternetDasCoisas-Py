notas = []

for x in range(3):
    n = float(input(f"Digite a nota da {x+1}º unidade: "))
    notas.append(n)

media = sum(notas)/3
print(f"\nMédia = {media:.1f}")