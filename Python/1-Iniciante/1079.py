# -*- coding:utf-8 -*-

quantity = int(input())
media_list = []

for x in range(0, quantity):
    a,b,c = map(float, input().split())
    media_list.append(
        (a * 2 + b * 3 + c * 5) / 10
    )

for x  in media_list:
    print('%.1f' %x)
