# -*- coding:utf-8 -*-

quantity = int(input())

for x in range(quantity):
    soma = 0
    number = int(input())
    for divisor in range(1, number):
        if number % divisor == 0:
            soma += divisor
    if soma == number:
        print('%d eh perfeito' % number)
    else:
        print('%d nao eh perfeito' % number)