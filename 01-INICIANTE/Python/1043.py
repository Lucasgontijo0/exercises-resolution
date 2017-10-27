# -*- coding:utf-8 -*-

medidas = map(float, input().split(" "))
a,b,c = medidas

if a + b > c and b + c > a and c + a > b:
    print('Perimetro = %.1f' %(a + b + c))
else:
    print('Area = %.1f' %((a + b)/2 * c ))