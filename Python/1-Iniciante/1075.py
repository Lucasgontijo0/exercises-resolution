# -*- coding: utf-8 -*-

num = int(input())

for x in range(1, 10000):
    if x % num == 2:
        print(x)
