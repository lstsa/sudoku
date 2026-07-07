
from board import exibir_board, resolver, today
from validator import jogada_valida
import arquivo
import random

dificuldades = {
    "facil": 46,
    "medio": 51,
    "dificil": 56
}


def gerar_puzzle(board, dificuldade):
    resolver(board)
    numero_de_celulas_a_remover = dificuldades[dificuldade]
    todas_as_celulas = [(i, j) for i in range(9) for j in range(9)]
    celulas_a_remover = random.sample(todas_as_celulas, numero_de_celulas_a_remover)
    celulas_imutaveis = list(set(todas_as_celulas) - set(celulas_a_remover))
    for i, j in celulas_a_remover:
        board[i][j] = 0
    return celulas_imutaveis

def obter_jogada(celulas_imutaveis):
    while True:
        print("Digite sua jogada no formato -> LinhaColunaDigito ex: 111")
        resposta = input("Resposta: ")
        
        if len(resposta) != 3:
            print("Sua resposta tem mais de 3 digitos.")
            continue
        
        if not resposta.isdigit():
            print("Sua resposta contém caracteres inválidos.")
            continue
        
        if any(x not in range(1, 10) for x in map(int, resposta)):
            print("Sua resposta contém números inválidos.")
            continue
        
        linha, coluna, digito = map(int, resposta)
        linha -= 1                
        coluna -= 1
        
        if (linha, coluna) in celulas_imutaveis:
            print("Essa célula já foi preenchida.")
            continue
        
        return linha, coluna, digito
    
def jogar(board, dificuldade):
    save = arquivo.carregar(today)
    if save[0] is not None:
        board, celulas_imutaveis, date = save
        print(f"Carregando save do dia {date}.")
    else:
        celulas_imutaveis = gerar_puzzle(board, dificuldade)
    exibir_board(board)
    while True:
        linha, coluna, digito = obter_jogada(celulas_imutaveis)
        if jogada_valida(board, linha, coluna, digito):
            board[linha][coluna] = digito
            arquivo.salvar(board, today, celulas_imutaveis)
            exibir_board(board)
            if not any(0 in row for row in board):
                print("Parabéns! Você completou o Sudoku!")
                return
        else:
            print("Jogada inválida. Tente novamente.")