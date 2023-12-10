#!/usr/bin/env python3

import regex as re

colors = { "red": 12, "green": 13, "blue": 14 }
sum = 0

with open('input.txt') as file:
    for line in file:
        (game, cubesets) = line.split(':')
        gamenr = int(re.findall(r'Game\s(\d+)', game)[0])
       
        doable = True 
        for cube in cubesets.split(';'):
            for color in colors:
                match = re.findall(r'(\d+)\s{}'.format(color), cube)
                if match:
                    if int(match[0]) > int(colors[color]):
                        doable = False
                        print("Not ok, {} or {} is over {}".format(match[0], color, colors[color]))

        if doable:
            sum += gamenr

print(sum)
            
