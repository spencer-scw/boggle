from dict import BoggleDictionary
from board import Board

import time
from copy import deepcopy
from threading import Timer

print("Welcome to Boggle!")
boggle_dicts ={
    "english": BoggleDictionary(),
    "spanish": BoggleDictionary('spanish')
}

def solve(board, dict, position = None, word_so_far = ''):
    solutions = set()
    if position == None:
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

def new_game(lang='english', time_sec=150):
    game_board = Board(lang)
    game_board.shake()
    for line in game_board.pretty():
        print(line)

    user_solutions = set()
    start = time.time()

    while time.time() - start < time_sec:
        solution = input('=> ')
        user_solutions.add(solution)

    all_solutions = solve(game_board, boggle_dicts[lang])

    score = 0
    for solution in user_solutions:
        if solution in all_solutions:
            score += len(solution) - 2
        else:
            print(f"{solution} is not in my dictionary.")

    print(f"Final score: {score}")

    print("Other solutions:")
    outstr = ''
    for i, solution in enumerate(sorted(all_solutions - user_solutions)):
        outstr = ''.join([outstr, solution, '\t'])
        if (i + 1) % 5 == 0:
            print(outstr)
            outstr = ''
    print(outstr)



def help():
    print("This is a Boggle game built in Python on the command line. It might have LAN multiplayer one day.")
    print("When you start a new game, a timer will begin and a boggle grid is printed. Type words on the command line that can be formed by chaining together the letters in cardinal or diagonal directions (no repeats). At the end of the timer, the program will check if your words are valid and assign points based on the length and number of valid words found.")
    print("The computer will also show you all of the possible words that you missed.")


while True:
    print()
    print("(n)ew game, (h)elp, (q)uit")
    print("for new games, you can specify the language and time limit in that order.")
    command, *args = input('-> ').split()
    if command in ['n', 'new', 'new game']:
        language = 'english'
        time_sec = 150
        if len(args) > 0:
            if args[0] in ['spanish']:
                language = args[0]
        if len(args) > 1:
            time_sec = int(args[1])
        new_game(language, time_sec)
    elif command in ['q', 'quit', 'exit']:
        break
    else:
        help()
