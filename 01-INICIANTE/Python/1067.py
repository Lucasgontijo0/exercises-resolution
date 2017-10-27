# -*- coding:utf-8 -*-

number = 0
impares = []

while number <= 1 or number >= 1000:
    number = int(input())

for x in range(1, number + 2):
    if x % 2 != 0:
        impares.append(x)

for x in impares:
    print(x)
