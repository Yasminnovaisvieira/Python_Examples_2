# Primeiro número da sequência de Fibonacci maior que 100.

x = 0
y = 1

while y <= 100:
    x, y = y, x + y

print(y)