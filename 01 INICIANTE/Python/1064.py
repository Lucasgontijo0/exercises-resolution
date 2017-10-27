# -*- coding: utf-8 -*-

numbers = list()
count = 0

for x in range(0, 6):
    value = float(input())
    if value >= 0:
        numbers.append(value)


media = sum(numbers) / len(numbers)
print('%d valores positivos' % len(numbers))
print('%.1f' % media)
