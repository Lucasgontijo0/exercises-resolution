# -*- coding: utf-8 -*-

quantity = 0
while quantity < 1 or quantity > 100:
    quantity = int(input())

for x in range(0, quantity):
    number = int(input())

    divisores = 0
    i = 1
    while i <= number:
        if number % i == 0:
            divisores += 1
        i += 1

    if divisores == 2:
        print('%d eh primo' % number)
    else:
        print('%d nao eh primo' % number)
