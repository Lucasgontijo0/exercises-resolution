# -*- coding:utf-8 -*-

par, imp, pos, neg = 0,0,0,0

for x in range(0, 5):
    num = int(input())
    if(num % 2 == 0):
        par += 1
    else:
        imp += 1
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1

print("%d valor(es) par(es)" % par)
print("%d valor(es) impar(es)" % imp)
print("%d valor(es) positivo(s)" % pos)
print("%d valor(es) negativo(s)" % neg)
