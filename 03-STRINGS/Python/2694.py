# -*- coding: utf-8 -*-
import re

quantity = 0
while quantity <= 0 or quantity  > 100000:
    quantity = int(input())

for x in range(0, quantity):
    entrada = input()
    numbers = list(map(int,re.findall(r'\d+', entrada)))
    soma = sum(numbers)
    print(soma)
