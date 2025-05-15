# Programa que calcula o maior palíndromo resultado do produto de dois números de 3 dígitos.

maior_palindromo = 0
x = 100

while x <= 999:
    y = x
    while y <= 999:
        produto = x * y
        if str(produto) == str(produto)[::-1]:
            if produto > maior_palindromo:
                maior_palindromo = produto
        y += 1
    x += 1

print(maior_palindromo)