def criar_board():
    board =[]
    lines = []
    
    
    for i in range(9):
        for j in range(9):
            lines.append(0)
        board.append(lines)
        lines = [] 
        
    return board

def exibir_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()
                        
board = criar_board()
exibir_board(board)