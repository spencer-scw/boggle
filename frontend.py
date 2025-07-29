import blessed
import functools
import multiprocessing
import time
from board import Board
from dict import BoggleDictionary
from solve import solve

term = blessed.Terminal()
echo = functools.partial(print, end='', flush=True)

def get_text():
    text = u''
    echo("=> ")
    while True:
        inp = term.inkey()
        if inp.code == term.KEY_ENTER:
            #print()
            break
        elif inp.code == term.KEY_ESCAPE or inp == chr(3):
            text = None
            break
        elif not inp.is_sequence:
            text += inp
            #echo(inp)
        elif inp.code in (term.KEY_BACKSPACE, term.KEY_DELETE):
            text = text[:-1]
            echo(u'\b \b')
    return text


def get_words():
    while True:
        user_solutions.append(get_text())

def show_timer(position, start, seconds):
    while True:
        elapsed = seconds + start - time.time()
        if elapsed <=0:
            with term.location(*position), term.hidden_cursor():
                print("Time left: 0    ")
        elif elapsed <= 6:
            with term.location(*position), term.hidden_cursor():
                print(f"Time left: {elapsed: .1f}     ")
        else:
            with term.location(*position), term.hidden_cursor():
                print(f"Time left: {int(elapsed)}    ")
        time.sleep(.1)

manager = multiprocessing.Manager()
user_solutions = manager.list()

def show_frontend(lang: str, time_sec: int):
    boggle_dict = BoggleDictionary(lang)      
    game_board = Board(lang)
    game_board.shake()
    all_solutions = solve(game_board, boggle_dict)
    with term.fullscreen():
        for line in game_board.pretty():
            print(line)

        p = multiprocessing.Process(target = get_words)
        p.start()

        start_time = time.time()
        timer = multiprocessing.Process(target=show_timer, args = ((20, 0), start_time, time_sec,))
        timer.start()

        timer.join(timeout = time_sec + .5)
   
        timer.terminate()
        p.terminate()

        p.join()
        timer.join()

        print()
        print("Time up!")

        score = 0
        for solution in user_solutions:
            solution = solution.strip()
            if solution in all_solutions:
                score += len(solution) - 2
            elif solution == '':
                pass
            elif len(solution) <= 2:
                print(f"{solution} is too short (words must be 3 or more letters.)")
            elif boggle_dict[solution] is None:
                print(f"{solution} is not in my dictionary.")
            else:
                print(f"{solution} is not possible on this board.")
        print(f"Final score: {score}")

        print("Other solutions:")
        outstr = ''
        for i, solution in enumerate(sorted(all_solutions - set(user_solutions))):
            outstr = ''.join([outstr, solution, '\t'])
            if (i + 1) % 5 == 0:
                print(outstr)
                outstr = ''
        print(outstr)
        
        print("Press any key to finish.")
        term.inkey()
