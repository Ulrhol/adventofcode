#!/usr/bin/env python3

import regex as re

trans = { 'one': 1,
          'two': 2,
          'three': 3,
          'four': 4,
          'five': 5,
          'six': 6,
          'seven': 7,
          'eight': 8,
          'nine': 9 }

sum = 0

finder = re.compile(r'\d|one|two|three|four|five|six|seven|eight|nine')

with open('input.txt') as file:
    for line in file:
        print('line: {}'.format(line.rstrip()))
        digits = finder.findall(line, overlapped=True)
        print('found: {}'.format(digits))
        fixed = []
        for digit in digits:
            if digit in trans:
                fixed.append(trans[digit])
            else:
                fixed.append(digit)
        print('partial sum: {} by adding {}'.format(sum, int('{}{}'.format(fixed[0],fixed[-1]))))
        sum += int('{}{}'.format(fixed[0],fixed[-1]))


print(sum)
       
