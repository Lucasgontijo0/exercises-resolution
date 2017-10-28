# -*- coding: utf-8 -*-

nums = []
qtd = int(input())

for num in range(1, (qtd + 1)):
    nums.append(int(input()))
for num in nums:
    if (num % 2 != 0)and (num < 0):
        print("ODD NEGATIVE")
    if(num == 0):
        print("NULL")
    if(num % 2 != 0) and (num > 0):
        print("ODD POSITIVE")
    if(num % 2 == 0) and (num < 0):
        print("EVEN NEGATIVE")
    if(num % 2 == 0) and (num > 0):
        print("EVEN POSITIVE")
