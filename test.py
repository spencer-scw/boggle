import blessed
import functools
import multiprocessing
import time

term = blessed.Terminal()
echo = functools.partial(print, end='', flush=True)

def get_text(start, timer_position, timer_seconds):
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


def get_words(words, timer_position, timer_seconds):
    start = time.time()
    while True:
        words.append(get_text(start, timer_position, timer_seconds))

def show_timer(position, start, seconds):
    elapsed = seconds + start - time.time()
    with term.location(*position), term.hidden_cursor():
        print(f"Time left: {elapsed: .1f}")
        

manager = multiprocessing.Manager()
words = manager.list()

with term.fullscreen():
    p = multiprocessing.Process(target = get_words, args = (words, (20, 0), 5,))
    p.start()

    #timer = multiprocessing.Process(target=show_timer, args = ((15, 0), 5,))
    #timer.start()
    
    p.join(timeout=5)
    p.terminate()
    p.join()
    print()
    print("time up. Your words: ")
    [print(word) for word in words]
    print("Press any key to finish.")
    term.inkey()
