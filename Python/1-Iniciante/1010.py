# -*- coding utf-8 -*-

totalValue = 0

for x in range(0, 2):
    line = input().split(" ")
    partCode, partQuantity, partValue = line
    totalValue += int(partQuantity) * float(partValue)


print('VALOR A PAGAR: R$ %.2f' % totalValue)
