def valida_linha(board, linha, numero):
    return numero not in board[linha]

def valida_coluna(board, coluna, numero):
    col = [board[i][coluna] for i in range(9)]
    return numero not in col

def valida_quadrante(board, linha, coluna, numero):
    start_row = (linha // 3) * 3
    start_col = (coluna // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == numero:
                return False
    return True

def jogada_valida(board,linha, coluna, numero):
    return (valida_linha(board, linha, numero) and
            valida_coluna(board, coluna, numero) and
            valida_quadrante(board, linha, coluna, numero))