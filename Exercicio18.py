# Fatorial de um número.

n = int(input("Digite o número que deseja fazer o fatorial: "))
contador = n
fatorial = 1

if n <= 0:
    print("Digite um número positivo!")
else:
    while contador > 1:
        fatorial *= contador
        contador -= 1
        print(fatorial)

print(f"O fatorial de {n} é: {fatorial}")