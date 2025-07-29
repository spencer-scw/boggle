from board import Board
from dict import BoggleDictionary
from copy import deepcopy

def solve(board: Board, dict: BoggleDictionary, position = None, word_so_far = ''):
    solutions = set()
    if position is None:
        for i in range(board.grid.shape[0]):
            for j in range(board.grid.shape[1]):
                new_board = deepcopy(board)
                new_board.grid[(i, j)] = '#'
                letter = board[(i, j)]
                solutions |= solve(new_board, dict, position = (i, j), word_so_far=letter)
        return solutions
    else:
        if dict[word_so_far].terminal and len(word_so_far) > 2:
            solutions.add(word_so_far)

        neighbors = board.neighbors(position)
        for neighbor in neighbors:
            letter = board[neighbor]
            if dict[word_so_far].get(letter) is not None:
                new_board = deepcopy(board)
                new_board.grid[neighbor] = '#'
                new_word_so_far = ''.join([word_so_far, letter])
                solutions |= solve(new_board, dict, neighbor, new_word_so_far)

        return solutions
