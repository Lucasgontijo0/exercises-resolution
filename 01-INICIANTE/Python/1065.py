# -*- coding:utf-8 -*-

numbers = []
count = 0
for x in range(0, 5):
    num = int(input())
    numbers.append(num)
    if num % 2 == 0:
        count += 1

print('%d valores pares' % count)
