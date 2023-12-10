#!/usr/bin/env python3

import regex as re
import json

extractor = re.compile(r'Card\s+(\d+):([\s\d]+)\|([\s\d]+)\n')
extractnr = re.compile(r'(\d+),*')

sum = 0

cards = {}

def checkwins(cardnr):
    wins = 0
    if cardnr not in cards:
        return(0)
    for nr in cards[cardnr]['winners']:
        if nr in cards[cardnr]['numbers']:
            wins += 1

    return(wins)

with open('input.txt') as file:
    for line in file:
        game = ""
        winners = []
        numbers = []
        for item in extractor.findall(line):
            game = str(item[0])
            cards[game] = { 'copies': 1, 'winners': [], 'numbers': [] }
            for winner in extractnr.finditer(item[1]):
                cards[game]['winners'].append(winner.group())
            for mynr in extractnr.finditer(item[2]):
                cards[game]['numbers'].append(mynr.group())

for card in cards:
    wins = checkwins(card)
    copies = int(cards[card]['copies'])
    for copy in range(int(card) + 1, int(card) + 1 + int(wins)):    
        if str(copy) in cards:
            cards[str(copy)]['copies'] += copies
            print("Adding {} copies of {}".format(copies, str(copy)))

for card in cards:
    if card in cards:
        sum += cards[card]['copies']
    
print(sum)    
