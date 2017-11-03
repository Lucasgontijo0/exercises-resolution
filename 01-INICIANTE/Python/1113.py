# -*- coding:utf-8 -*-

while True:
    x, y = map(int, input().split())
    if x < y:
        print("Crescente")
    elif y < x:
        print("Decrescente")
    else:
        break
