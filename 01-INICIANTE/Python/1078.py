# -*- coding:utf-8 -*-

number = 0
while number < 2 or number > 1000:
    number = int(input())

for x in range(1,11):
    print('%d x %d = %d' %(x, number, x * number))
