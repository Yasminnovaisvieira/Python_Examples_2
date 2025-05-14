# Faixa etária.

idade = int(input("Digite a idade: "))

if idade >= 0 and idade <= 12:
    print(f"Faixa etária: INFANTIL!")
elif idade >= 13 and idade <= 17:
    print("Faixa etária: ADOLESCENTE!")
elif idade >= 18 and idade <= 64:
    print("Faixa etária: ADULTO!")
elif idade >= 65:
    print("Faixa etária: IDOSO!")
else:
    print("Digite uma idade maior que zero.")