# -*- coding: utf-8 -*-

numbers = list()

for x in range(0, 6):
    value = int(input())
    if value >= 0:
        numbers.append(value)

print('%d valores positivos' % len(numbers))
