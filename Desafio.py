# Sistema de comando de uma loja de jogos.

import tkinter as tk
from tkinter import messagebox # Usado para mostrar mensagem de erro ou confirmação

jogos_disponiveis = ["Labyrinthine", "Minecraft", "Phasmophobia", "The Outlast Trials"]
preco_jogos = [69.90, 31.60, 42.50, 229.90]
quantidade_jogos_disponiveis = [4, 7, 8, 5]
preco_fabrica_jogos = [49.40, 19.98, 37.70, 164.88]
valor_caixa = 4324.00
vendas = []
compras = []

def registrar_venda():
    janela_venda = tk.Toplevel() # Cria uma nova tela independente da inicial
    janela_venda.title("Registrar Venda") # Título dessa nova janela

    tk.Label(janela_venda, text="Selecione o jogo vendido:").pack(pady=10) # Colocar texto na tela

    for i in range(len(jogos_disponiveis)): # Lembrando: Len é para retornar número/quantidade
        texto = f"{jogos_disponiveis[i]} - R${preco_jogos[i]:.2f} - Estoque: {quantidade_jogos_disponiveis[i]}" # Aparecerá ao clicar no botão
        botao = tk.Button(janela_venda, text=texto, width=50,
                          command=lambda i=i: efetuar_venda(i, janela_venda)) # Define o que o botão irá fazer ao ser clicado
        botao.pack(pady=2) # Espaço vertical

def efetuar_venda(indice, janela):
    global valor_caixa # Variável global para que ela possa ser modificada caso precise
    if quantidade_jogos_disponiveis[indice] > 0: # Verifica se ainda há o produto no estoque
        quantidade_jogos_disponiveis[indice] -= 1
        valor_caixa += preco_jogos[indice]
        vendas.append((jogos_disponiveis[indice], preco_jogos[indice]))
        messagebox.showinfo("Venda registrada", f"Venda: {jogos_disponiveis[indice]} por R${preco_jogos[indice]:.2f}") # Mensagem informando sucesso
        janela.destroy() # Para fechar a janela
    else:
        messagebox.showwarning("Erro", "Estoque esgotado para esse jogo.") # Mensagem informando erro

def registrar_compra():
    janela_compra = tk.Toplevel() # Tela independente
    janela_compra.title("Compra de Estoque") # Título da tela

    tk.Label(janela_compra, text="Selecione o jogo para reabastecimento:").pack(pady=10) # Texto que será mostrado na tela

    for i in range(len(jogos_disponiveis)): # Cria um botão específico para cada jogo que mostra o nome do jogo e o preço de fábrica dele, e, ao clicar. Ao clicar, pergunta quantas unidades quer comprar daquele jogo.
        texto = f"{jogos_disponiveis[i]} - Preço fábrica: R${preco_fabrica_jogos[i]:.2f}"
        botao = tk.Button(janela_compra, text=texto, width=50,
                          command=lambda i=i: pedir_quantidade(i, janela_compra))
        botao.pack(pady=2)

def pedir_quantidade(indice, janela_anterior): # Jogo selecionado e qual era a janela anterior para que essa possa ser fechada
    janela_qtd = tk.Toplevel()
    janela_qtd.title("Quantidade para Compra")

    tk.Label(janela_qtd, text=f"Quantas unidades deseja comprar de {jogos_disponiveis[indice]}?").pack(pady=10)
    entrada_qtd = tk.Entry(janela_qtd)
    entrada_qtd.pack() # Organizar os widgets dentro da janela

    def confirmar_compra(): # Para confirmar a compra
        global valor_caixa
        try:
            qtd = int(entrada_qtd.get()) # Transformar o número/valor que usuário colocou para inteiro
            custo_total = qtd * preco_fabrica_jogos[indice] # Total da compra

            if valor_caixa >= custo_total: # Se há dinheiro o suficiente
                quantidade_jogos_disponiveis[indice] += qtd # Aumenta o estoque
                valor_caixa -= custo_total # Subtrai o valor da compra
                compras.append((jogos_disponiveis[indice], qtd, custo_total)) # Registra compra
                messagebox.showinfo("Compra registrada", f"Compra de {qtd} unidades registrada com sucesso.") # Mensagem de sucesso
                janela_qtd.destroy() # Fecha janela atual
                janela_anterior.destroy() # Fecha janela anterior
            else:
                messagebox.showerror("Erro", "Dinheiro insuficiente no caixa.")
        except ValueError:
            messagebox.showerror("Erro", "Digite uma quantidade válida.") # Mensagem caso dê erro

    tk.Button(janela_qtd, text="Confirmar", command=confirmar_compra).pack(pady=5) # Botão para confirmar

def mostrar_resumo():
    janela_resumo = tk.Toplevel()
    janela_resumo.title("Resumo da Loja")

    tk.Label(janela_resumo, text="=== ESTOQUE ATUAL ===").pack(pady=5)
    for i in range(len(jogos_disponiveis)):
        texto = f"{jogos_disponiveis[i]} | R${preco_jogos[i]:.2f} | Quantidade: {quantidade_jogos_disponiveis[i]}"
        tk.Label(janela_resumo, text=texto).pack()

    tk.Label(janela_resumo, text="\n=== VENDAS ===").pack(pady=5)
    total_vendas = sum(venda[1] for venda in vendas)
    for venda in vendas:
        tk.Label(janela_resumo, text=f"{venda[0]} - R${venda[1]:.2f}").pack()
    tk.Label(janela_resumo, text=f"Total em vendas: R${total_vendas:.2f}").pack()

    tk.Label(janela_resumo, text="\n=== COMPRAS ===").pack(pady=5)
    total_gastos = sum(compra[2] for compra in compras)
    for compra in compras:
        tk.Label(janela_resumo, text=f"{compra[1]}x {compra[0]} - R${compra[2]:.2f}").pack()
    tk.Label(janela_resumo, text=f"Total em compras: R${total_gastos:.2f}").pack()

    tk.Label(janela_resumo, text=f"\nDinheiro atual em caixa: R${valor_caixa:.2f}").pack(pady=10)

janela_principal = tk.Tk() # Criação de janela inicial
janela_principal.title("YasGames") # Título da janela
janela_principal.geometry("500x250") # Tamanho da janela inicial

tk.Label(janela_principal, text="Bem-vindo ao Sistema de Loja YasGames", font=("Arial", 16)).pack(pady=20) # Titulo janela inicial

frame_menu = tk.Frame(janela_principal) # Para organizar widgets
frame_menu.pack() # Ocupar espaço disponível

# Botões na janela inicial
tk.Button(frame_menu, text="Registrar Venda", width=20, height=2, command=registrar_venda).grid(row=0, column=0, padx=10, pady=10)
tk.Button(frame_menu, text="Compra de Estoque", width=20, height=2, command=registrar_compra).grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame_menu, text="Resumo da Loja", width=20, height=2, command=mostrar_resumo).grid(row=1, column=0, padx=10, pady=10)
tk.Button(frame_menu, text="Sair", width=20, height=2, command=janela_principal.destroy).grid(row=1, column=1, padx=10, pady=10)

janela_principal.mainloop() # Esperar interação