# -*- coding: utf-8 -*-

import math

line = map(float, input().split(" "))
x1, y1 = line

line = map(float, input().split(" "))
x2, y2 = line

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print('%.4f' % distance)
