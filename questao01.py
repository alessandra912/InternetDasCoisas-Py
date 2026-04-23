idades = []

while True:
    idade = int(input("Digite uma idade (-1 para parar): "))

    if idade == -1:
        break

    idades.append(idade)

if len(idades) > 0:
    quantidade = len(idades)
    media = sum(idades) / quantidade
    maiores_18 = sum(1 for idade in idades if idade >= 18)

else:
    quantidade = 0
    media = 0 
    maiores_18 = 0

print("\nResultados:")
print("\nLista de idades: ", idades)
print("Quantidade de idades: ", quantidade)
print("Média de idades: ", media)
print("Idades maiores ou iguais a 18 anos: ", maiores_18)


# idade = []
#
# while True:
#     idade = int(input("Digite uma idade (-1 para parar): "))
#     if(i == -1):
#         break
#     else:
#       idade.append(i)
#
# contagem = 0
#
# for x in idade:
#   print(x, end='\n|')
#   if(x>=18):
#       contagem = contagem+1
#
# media = sum(idade)/le(idade)
# print(f"\nA média das idades é {idade:.0f}: )
# print(f"\nIdades maiores ou iguais a 18 anos:)