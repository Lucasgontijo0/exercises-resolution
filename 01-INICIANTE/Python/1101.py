# -*- coding:utf-8 -*-

cond = True
while cond:
    x, y = map(int,input().split())
    
    if x <= 0 or y <=0:
        cond = False
    else:
        start = min(x, y)
        end = max(x, y)

        soma = 0
        interval = ''
        for x in range(start, end + 1):
            interval += '%d ' % x
            soma += x
        interval = interval[:-1] # Remove last string character.
        print('%s Sum=%d' %(interval,soma))
