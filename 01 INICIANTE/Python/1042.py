# -*- coding: utf-8 -*-

originalNumbers = list(map(int, input().split(" ")))
newNumbers = originalNumbers.copy()

newNumbers.sort()

for x in newNumbers:
    print(x)

print()

for x in originalNumbers:
    print(x)
