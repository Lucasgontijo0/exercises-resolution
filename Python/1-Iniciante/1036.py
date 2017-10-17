# -*- coding:utf-8 -*-
import math

numbers = map(float, input().split(" "))
a, b, c = numbers

delta = ((b ** 2) - 4 * a * c)
if delta < 0 or a == 0 or c == 0:
    print ('Impossivel calcular')
else:
    x = math.sqrt(delta)
    x1 = (- b + x) / (2 * a)
    x2 = (- b - x) / (2 * a)
    print('R1 = %.5f' % x1)
    print('R2 = %.5f' % x2)
