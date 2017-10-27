# -*- coding:utf-8 -*-

numbers = []

maior = 0
pos = 0
for x in range(0, 100):
    num = int(input())
    numbers.append(num)
    if num > maior:
        maior = num
        pos = x + 1

print(maior)
print(pos)