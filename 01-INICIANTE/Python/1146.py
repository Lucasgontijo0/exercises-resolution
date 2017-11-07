# -*- coding: utf-8 -*-

cond = True

alcool = 0
gasolina = 0
diesel = 0
while cond:
    num = int(input())
    if num == 1:
        alcool += 1
    elif num == 2:
        gasolina += 1
    elif num == 3:
        diesel += 1
    elif num == 4:
        cond = False

print('MUITO OBRIGADO')
print('Alcool: %d' % alcool)
print('Gasolina: %d' % gasolina)
print('Diesel: %d' % diesel)
