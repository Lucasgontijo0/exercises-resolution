# -*- coding: utf-8 -*-

value = int(input())

cedulasCem = int(value / 100)
cedulasCinquenta = int((value % 100) / 50)
cedulasVinte = int(((value % 100) % 50) / 20)
cedulasDez = int((((value % 100) % 50) % 20) / 10)
cedulasCinco = int(((((value % 100) % 50) % 20) % 10) / 5)
cedulasDois = int((((((value % 100) % 50) % 20) % 10) % 5) / 2)
cedulasUm = int(((((((value % 100) % 50) % 20) % 10) % 5) % 2) / 1)

print(value)
print('%d nota(s) de R$ 100,00' % cedulasCem)
print('%d nota(s) de R$ 50,00' % cedulasCinquenta)
print('%d nota(s) de R$ 20,00' % cedulasVinte)
print('%d nota(s) de R$ 10,00' % cedulasDez)
print('%d nota(s) de R$ 5,00' % cedulasCinco)
print('%d nota(s) de R$ 2,00' % cedulasDois)
print('%d nota(s) de R$ 1,00' % cedulasUm)
