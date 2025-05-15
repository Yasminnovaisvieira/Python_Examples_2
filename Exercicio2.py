# Numéro positivo, negativo ou zero.

numero = float(input("Digite o número: "))

if numero < 0:
    print(f"{numero} é NEGATIVO!")
elif numero == 0:
    print(f"{numero} é ZERO!")
else:
    print(f"{numero} é POSITIVO!")