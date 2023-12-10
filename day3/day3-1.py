#!/usr/bin/env python

import regex as re
import json

nrextract = re.compile(r'(\d+)')
symextract = re.compile(r'([^\d\.\n])')

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
    for nr in filerep[str(line)]:
        for checkline in range(line - 1, line + 2):
            for pos in range(filerep[str(line)][nr]['start']-1, filerep[str(line)][nr]['end']+1):
                if str(checkline) in symbols:
                    if str(pos) in symbols[str(checkline)]:
                        sum += int(filerep[str(line)][nr]['nr'])
                    

print(sum)
