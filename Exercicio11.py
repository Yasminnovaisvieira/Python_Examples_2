# Impressão de cada caractere de uma string em uma linha separada.

string = str(input("Digite uma frase: "))

for caractere in string:
    print(caractere, end="\n")