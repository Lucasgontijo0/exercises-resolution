# -*- coding:utf-8 -*-

quantity = int(input())

for val in range(0, quantity):
    x, y = map(int, input().split())

    begin = min(x,y)
    end = max(x,y)

    soma = 0
    for num in range(begin + 1, end):
        if num % 2 != 0:
            soma += num
    print(soma)