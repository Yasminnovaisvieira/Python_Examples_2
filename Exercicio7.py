# Verificar se o aluno está aprovado, reprovado ou em recuperação.

aluno = str(input("Digite o nome do aluno(a): "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media > 7:
    print(f"o aluno {aluno} está APROVADO! ")
elif media >= 5 and media < 7:
    print(f"O aluno {aluno} está EM RECUPERAÇÃO!")
elif media >= 0 and media < 5:
    print(f"O aluno {aluno} está REPROVADO!")
else:
    print("ERRO!")