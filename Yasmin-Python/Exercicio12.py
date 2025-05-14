# Lista com o quadrado de cada número em outra lista.

lista = [1,2,3,4,5,6,7,8,9,10]
quadrado = 0
quadrados =[]

for numero in lista:
    quadrados.append(numero * numero)

print(quadrados)