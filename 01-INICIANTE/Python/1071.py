# -*- coding:utf-8 -*-

x = int(input())
y = int(input())

start = min(x, y)
end = max(x, y)

soma = 0
for x in range(start + 1, end):
    if x % 2 != 0:
        soma += x
print(soma)