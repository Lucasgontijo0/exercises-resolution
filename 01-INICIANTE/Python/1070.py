# -*- coding:utf-8 -*-

number = int(input())
impares = []

if number % 2 == 0:
    number += 1

for x in range(0, 6):
    impares.append(number)
    number += 2

for x in impares:
    print(x)
