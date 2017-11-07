# -*- coding: utf-8 -*-

x = int(input())
y = int(input())

begin = min(x, y)
end = max(x, y)

soma = 0
for num in range(begin, end + 1):
    if(num % 13 != 0):
        soma += num

print(soma)