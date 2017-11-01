# -*- coding: utf-8 -*-

num = 0

while num > 10000 or num == 0:
    num = int(input())

for x in range(1, 10000):
    if x % num == 2:
        print(x)