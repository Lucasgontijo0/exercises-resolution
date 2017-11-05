# -*- coding:utf-8 -*-

size = 0
while size < 1 or size > 1000:
    size = int(input())

for x in range(1, size + 1):
    print("%d %d %d" %(x, x ** 2, x ** 3))
    
