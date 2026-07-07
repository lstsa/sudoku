from board import criar_board
from game import jogar, dificuldades


board = criar_board()
dificuldade = input("Escolha a dificuldade (facil, medio, dificil): ").lower()
while dificuldade not in dificuldades:
    print("Dificuldade inválida. Tente novamente.")
    dificuldade = input("Escolha a dificuldade (facil, medio, dificil): ").lower()
jogar(board, dificuldade)