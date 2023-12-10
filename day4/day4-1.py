#!/usr/bin/env python3

import regex as re

extractor = re.compile(r'Card\s+(\d+):([\s\d]+)\|([\s\d]+)\n')
extractnr = re.compile(r'(\d+),*')

sum = 0

with open('input.txt') as file:
    for line in file:
        game = ""
        winners = []
        numbers = []
        for item in extractor.findall(line):
            game = str(item[0])
            for winner in extractnr.finditer(item[1]):
                winners.append(winner.group())
            for mynr in extractnr.finditer(item[2]):
                numbers.append(mynr.group())

        print("Game {} Winners: {} My numbers: {}".format(game, ','.join(winners), ','.join(numbers)))
        win = 0
        for item in winners:
            if item in numbers:
                print("Hit: {}".format(item))
                if win == 0:
                    win += 1
                else:
                    win *= 2

        print("Points: {}".format(win))
        sum += win
print(sum)
            
