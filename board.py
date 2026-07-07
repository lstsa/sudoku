import random
from datetime import date
from validator import jogada_valida

today = date.today()
random.seed(str(today))

def criar_board():
    board =[]
    line = []
    
    for i in range(9):
        for j in range(9):
            line.append(0)
        board.append(line)
        line = [] 
        
    return board

def exibir_board(board):
    for index, line in enumerate(board):             
        if index % 3 == 0 and index != 0:
            print("-" * 21)
        for index_column, column in enumerate(line):
            if index_column % 3 == 0 and index_column != 0:
                print("|", end=" ")
            print(column, end=" ")
        print()
          
def resolver(board):
    if not any(0 in row for row in board):
        return True
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                numeros = list(range(1, 10))
                random.shuffle(numeros)
                for numero in numeros:
                    if jogada_valida(board, i, j, numero):
                        board[i][j] = numero
                        if resolver(board):
                            return True
                        board[i][j] = 0
                return False
    return True   
        