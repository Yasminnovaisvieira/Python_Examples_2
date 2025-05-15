# Programa que imprime os n primeiros múltiplos de 5, sendo n definido pelo usuário.

numero = int(input("Digite um número: "))

for i in range(1, numero+1):
    multiplo = i * 5
    print(multiplo, end=" ")