# -*- coding:utf-8 -*-

quantity = int(input())

number = 1
for x in range(0, quantity):
    pum = ''
    for y in range(number, number + 3):
        if y % 4 != 0:
            pum += '%d ' % y
    number += 4
    print('%sPUM' % pum)
