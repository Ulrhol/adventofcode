#!/usr/bin/env python

import regex as re
import json

nrextract = re.compile(r'(\d+)')
symextract = re.compile(r'(\*)')

filerep = {}
symbols = {}

linenr = 0
sum = 0

with open('input.txt') as file:
    for line in file:
        obj = 0
        for m in nrextract.finditer(line):
            if str(linenr) not in filerep:
                filerep[str(linenr)] = {}
            filerep[str(linenr)][str(obj)] = { 'nr': m.group(), 'start': m.start(), 'end': m.end() }
            obj += 1

        for m in symextract.finditer(line):
            if str(linenr) not in symbols:
                symbols[str(linenr)] = {}
            symbols[str(linenr)][str(m.start())] = m.group()

        linenr += 1

for line in range(0, linenr):
    if str(line) in symbols:
        for pos in symbols[str(line)]:
            hits = []
            print("Checking * symbol at {}:{}".format(line, pos))
            for checkline in range(line - 1, line + 2):
                for posrage in range(int(pos), int(pos) + 3):
                    # print("Checking: {}:{}".format(checkline, posrage))
                    if str(checkline) in filerep:
                        for nr in filerep[str(checkline)]:
                            number = filerep[str(checkline)][nr]
                            if number['start'] < posrage < number['end'] + 1:
                                print("Hit on {}".format(number['nr']))
                                if number['nr'] not in hits:
                                    hits.append(number['nr'])
            if len(hits) == 2:
                print("Adding sum of {} * {}".format(int(hits[0]),int(hits[1])))
                sum += int(hits[0]) * int(hits[1])

# print(json.dumps(symbols, indent=2))
print(sum)
