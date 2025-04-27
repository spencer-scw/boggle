import numpy as np

class Die:
    def __init__(self, letters):
        self.letters = np.array(letters)

    def roll(self):
        return np.random.choice(self.letters).item()

class Board:
    def __init__(self, language, size = 4):
        self.grid = np.empty([size, size], dtype = str)
        self.dice = []
        self.size = size

        dice_letters = ''.join([language, '.txt'])
        f = open(dice_letters, 'r')
        dice_lines = f.readlines()

        for line in dice_lines:
            line = line.strip().lower()
            new_die = Die(line.split(','))
            self.dice.append(new_die)

    def __getitem__(self, position):
        return self.grid[position]

    def shake(self):
        np.random.shuffle(self.dice)
        dice_iter = iter(self.dice)
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i, j] = next(dice_iter).roll()

    def neighbors(self, pos):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) + abs(j) > 0:
                    newpos = (pos[0] + i, pos[1] + j)
                    if newpos[0] >= 0 and newpos[1] >= 0 and newpos[0] < self.size and newpos[1] < self.size:
                        neighbors.append(newpos)
        return neighbors

    def pretty(self):
        f = open('pretty.txt', 'r')
        out = []
        letters = iter(self.grid.flatten())
        for line in f.readlines():
            while line.find('#') >= 0:
                index = line.find('#')
                line = ''.join([line[:index], next(letters), line[index + 1:]])
            out.append(line.strip())

        return out
                

