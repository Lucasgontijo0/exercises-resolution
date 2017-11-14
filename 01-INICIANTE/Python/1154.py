# -*- coding: utf-8 -*-

quantity = 0
soma = 0
while True:
    entrada = int(input())
    if entrada > 0:
        quantity += 1
        soma += entrada
    else:
        break

try:
    print('%.2f' %(soma / quantity))
except ZeroDivisionError:
    pass
