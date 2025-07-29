from blessed import Terminal
from functools import partial
from time import time

echo = partial(print, end='', flush=True)
term = Terminal()
start = time()

with term.fullscreen(), term.cbreak(), term.hidden_cursor():
    while time() - start < 10:
        with term.location():
            print(term.home + term.clear)
        print(time() - start)

# echo(term.move_y(term.height) + '=> ')
# with term.cbreak(), term.fullscreen():
#     val = term.inkey()
#     while time() - start < 3:# and val.name != 'KEY_ESCAPE':
#         print(time() - start)
#         val = term.inkey()
#         if val.is_sequence:
#             if val.name == 'KEY_ENTER':
#                 echo(term.move_y(term.height) + '=> ')
#             else:
#                 echo(val)
#         elif val:
#             echo(val)
#     print()
#     print(f'bye!{term.normal}')
