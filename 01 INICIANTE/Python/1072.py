# -*- coding:utf-8 -*-

num = int(input())
numbers = []

for x in range(0, num):
    numbers.append(int(input()))

numIn = 0
numOut = 0
for x in numbers:
    if x >= 10 and x <= 20:
        numIn += 1
    else:
        numOut += 1

print('%d in' % numIn)
print('%d out' % numOut)