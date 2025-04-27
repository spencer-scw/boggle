from play import new_game, help

def main():
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


if __name__ == "__main__":
    main()
