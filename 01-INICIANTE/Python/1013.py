# -*- coding: utf-8 -*-

line = map(float, input().split(" "))
a, b, c = line

result = (a + b + abs(a - b)) / 2
maior = (result + c + abs(result - c)) / 2

print('%d eh o maior' % maior)
