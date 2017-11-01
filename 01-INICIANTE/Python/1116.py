# -*- coding:utf-8 -*-

quantity = int(input())

for x in range(quantity):
    dividendo, divisor = map(int, input().split())
    try:
        print(dividendo / divisor)
    except:
        print('divisao impossivel')
