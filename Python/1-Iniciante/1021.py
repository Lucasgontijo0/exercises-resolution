# -*- coding: utf-8 -*-

number = 0
while number <= 0 or number >= 1000000.00:
    number = float(input())

cedulasCem = number / 100
cedulasCinq = number % 100 / 50
cedulasVint = (number % 100 % 50) / 20
cedulasDez = (number % 100 % 50 % 20) / 10
cedulasCinco = (number % 100 % 50 % 20 % 10) / 5
cedulasDois = (number % 100 % 50 % 20 % 10 % 5) / 2

moedas = round(number % 1, 2)
moedaUm = (number % 100 % 50 % 20 % 10 % 5 % 2) / 1
moedaCinquenta = moedas / 0.50
moedaVinteCinco = moedas % 0.50 / 0.25
moedaDez = moedas % 0.50 % 0.25 / 0.10
moedaCinco = moedas % 0.50 % 0.25 % 0.10 / 0.05
moedaUmCent = round(moedas % 0.50 % 0.25 % 0.10 % 0.05 / 0.01, 1)

print('NOTAS:')
print('%d nota(s) de R$ 100.00' % cedulasCem)
print('%d nota(s) de R$ 50.00' % cedulasCinq)
print('%d nota(s) de R$ 20.00' % cedulasVint)
print('%d nota(s) de R$ 10.00' % cedulasDez)
print('%d nota(s) de R$ 5.00' % cedulasCinco)
print('%d nota(s) de R$ 2.00' % cedulasDois)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' % moedaUm)
print('%d moeda(s) de R$ 0.50' % moedaCinquenta)
print('%d moeda(s) de R$ 0.25' % moedaVinteCinco)
print('%d moeda(s) de R$ 0.10' % moedaDez)
print('%d moeda(s) de R$ 0.05' % moedaCinco)
print('%d moeda(s) de R$ 0.01' % moedaUmCent)
