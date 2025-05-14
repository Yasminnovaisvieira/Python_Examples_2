# Calculo da média de uma lista de números.

lista = [1,2,3,4,5,6,7,8,9,10]
soma = 0

for numero in lista:
    soma += numero
    media = soma / 10

print(f"A média é: {media:.2f}")