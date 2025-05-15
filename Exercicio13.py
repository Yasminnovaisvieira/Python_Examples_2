# Programa que calcula a soma dos divisores de um número inteiro definido pelo usuário.

numero = int(input("Digite um número: "))
soma_divisores = 0
lista_divisores = []

for i in range (1, numero+1):
    if numero % i == 0:
        soma_divisores += i
        lista_divisores.append(i)

print(f"O resultado da soma dos divisores {lista_divisores} de {numero} é: {soma_divisores}")