# -*- coding:utf-8 -*-

size = 0
while size < 5 or size > 2000:
    size = int(input())

for x in range(1, size + 1):
    if x % 2 == 0:
        print ("%d^2 = %d" %(x, x ** 2))
