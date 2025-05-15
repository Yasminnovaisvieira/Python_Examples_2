# Impressão dos primeiros 5 números pares.

numeros_pares = 0
numero_atual = int(input("Digite o número inicial da sequência que deseja verificar os 5 números pares: "))

while numeros_pares < 5:
    if numero_atual % 2 == 0:
        print(f"Número {numero_atual} é PAR!")
        numeros_pares += 1
    numero_atual += 1

