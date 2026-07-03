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
                        
board = criar_board()
exibir_board(board)