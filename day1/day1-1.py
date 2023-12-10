#!/usr/bin/env python3

import re

sum = 0

with open('input.txt') as file:
    for line in file:
        digits = re.findall('\d', line)
        print('{}{}'.format(digits[0],digits[-1]))
        sum += int('{}{}'.format(digits[0],digits[-1]))
        print(sum)


print(sum)
       
