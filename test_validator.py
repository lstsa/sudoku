from validator import jogada_valida
import pytest

def test_valida_linha_num_ausente():
    board = [[1, 2, 3, 4, 5, 6, 7, 8, 0]] + [[0] * 9] * 8
    assert jogada_valida(board, 0, 0, 9) == True
    
def test_valida_linha_num_presente():
    board = [[1, 2, 3, 4, 5, 6, 7, 8, 9]] + [[0] * 9] * 8
    assert jogada_valida(board, 0, 0, 5) == False
    
def test_valida_quadrante_num_ausente():
    board = [[1, 2, 3] + [0] * 6] + [[0] * 9] * 8
    assert jogada_valida(board, 1, 1, 4) == True
    
def test_valida_quadrante_num_presente():
    board = [[1, 2, 3] + [0] * 6] + [[0] * 9] * 8
    assert jogada_valida(board, 1, 1, 2) == False

def test_valida_coluna_num_ausente():
    board = [[1] + [0] * 8] + [[0] * 9] * 8
    assert jogada_valida(board, 1, 0, 2) == True

def test_valida_coluna_num_presente():
    board = [[1] + [0] * 8] + [[0] * 9] * 8
    assert jogada_valida(board, 1, 0, 1) == False