# -*- coding: utf-8 -*-

x = int(input())
y = int(input())

maior, menor = max(x, y), min(x, y)

for x in range(menor + 1, maior):
    if x % 5 == 2 or x % 5 == 3:
        print(x)
