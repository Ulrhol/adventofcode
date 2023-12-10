#!/usr/bin/env python3

import regex as re

sum = 0

with open('input.txt') as file:
    for line in file:
        colors = { "red": 0, "green": 0, "blue": 0 }
        (game, cubesets) = line.split(':')
        gamenr = int(re.findall(r'Game\s(\d+)', game)[0])
       
        doable = True 
        for cube in cubesets.split(';'):
            for color in colors:
                match = re.findall(r'(\d+)\s{}'.format(color), cube)
                if match:
                    if int(match[0]) > int(colors[color]):
                        colors[color] = int(match[0])

        power = 1
        for color in colors:
            power *= colors[color]

        print("game {}, power = {}".format(gamenr, power))
        sum += power

print(sum)
            
