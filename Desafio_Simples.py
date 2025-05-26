# Sistema de comando de uma loja de jogos.

jogos_disponiveis = ["Labyrinthine", "Minecraft", "Phasmophobia", "The Outlast Trials"]
preco_jogos = [69.90, 31.60, 42.50, 229.90]
quantidade_jogos_disponiveis = [4, 7, 8, 5] # Quantidade baixa para testes
preco_fabrica_jogos = [49.40, 19.98, 37.70, 164.88]
vendas = [] # Registrar as vendas
compras = [] # Registrar as compras
valor_caixa = 4324 # Valor inicial do caixa

while True:
    print("\n=== MENU - LOJA DE JOGOS (YASGAMES) ===")
    print("\n1 - Registrar venda.")
    print("2 - Compra de estoque.")
    print("3 - Resumo da Loja.")
    print("4 - Sair.")

    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == "1":
        print("\n=== Jogos disponíveis para venda ===\n")
        for i in range(len(jogos_disponiveis)):
            print(f"{i + 1} - {jogos_disponiveis[i]} | R${preco_jogos[i]:.2f} | Estoque: {quantidade_jogos_disponiveis[i]} ainda disponíveis")

        escolha = int(input("\nDigite o número do jogo vendido: ")) - 1

        if escolha >= 0 and escolha < len(jogos_disponiveis):
            if quantidade_jogos_disponiveis[escolha] > 0:
                quantidade_jogos_disponiveis[escolha] -= 1 # Tira produto comprado do estoque

                valor_caixa += preco_jogos[escolha] # Adiciona o valor da venda no caixa

                vendas.append((jogos_disponiveis[escolha], preco_jogos[escolha])) # Registra a venda com o nome e valor

                print(f"Venda registrada: {jogos_disponiveis[escolha]} por R${preco_jogos[escolha]:.2f}")
            else:
                print("Estoque esgotado para esse jogo!")
        else:
            print("Número inválido.")

    elif opcao == "2":
        print("\n=== Jogos para reabastecimento ===")
        for i in range(len(jogos_disponiveis)):
            print(f"{i + 1} - {jogos_disponiveis[i]} | Preço fábrica: R${preco_fabrica_jogos[i]:.2f}")

        escolha = int(input("\nDigite o número do jogo para comprar: ")) - 1

        if escolha >= 0 and escolha < len(jogos_disponiveis):
            qtd = int(input("Quantas unidades deseja comprar? "))

            custo_total = qtd * preco_fabrica_jogos[escolha]  # Calcula o valor total da compra

            if valor_caixa >= custo_total:
                quantidade_jogos_disponiveis[escolha] += qtd  # Aumenta o estoque
                valor_caixa -= custo_total  # Diminui o dinheiro no caixa
                compras.append((jogos_disponiveis[escolha], qtd, custo_total))  # Registra a compra

                print(f"Compra registrada: {qtd} unidades de {jogos_disponiveis[escolha]} por R${custo_total:.2f}")
            else:
                print("Dinheiro insuficiente no caixa para essa compra!")
        else:
            print("Número inválido.")

    elif opcao == "3":
        print("\n=== RESUMO DA LOJA ===")

        for i in range(len(jogos_disponiveis)): # Mostra todos os jogos, seus preços e suas quantidades
            print(f"{jogos_disponiveis[i]} | R${preco_jogos[i]:.2f} | Quantidade: {quantidade_jogos_disponiveis[i]}")

        print("\n=== VENDAS ===") # Mostra todas as vendas realizadas
        total_vendas = 0
        for venda in vendas:
            print(f"{venda[0]} - R${venda[1]}")
            total_vendas += venda[1]
        print(f"Valor total em relação as vendas: R${total_vendas:.2f}")

        print("\n=== COMPRAS DE ESTOQUE ===")
        total_gastos = 0
        for compra in compras: # Mostra todas as compras realizadas
            print(f"{compra[1]}x {compra[0]} - R${compra[2]}")
            total_gastos += compra[2]
        print(f"Valor total de gastos com compras: R${total_gastos:.2f}")

        print(f"\nDinheiro atual em caixa: R${valor_caixa:.2f}") # Mostra o saldo atual do caixa

    elif opcao == "4":
        print("\nCaixa fechado! Sistema encerrado.")
        break