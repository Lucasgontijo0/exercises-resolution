# -*- coding: utf-8 -*-

cond = True

while cond:
    num = int(input())
    output = ''
    if num == 0:
        cond = False
    for x in range(1, num+1):
        output += '%d ' % x
    output = output[:-1]

    if output != '':
        print(output)
