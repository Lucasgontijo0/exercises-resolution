# -*- coding: utf-8 -*-

name = input()
salary = float(input())
totalSales = float(input())

totalToReceive = salary + 0.15 * totalSales

print('TOTAL = R$ %.2f' % totalToReceive)
