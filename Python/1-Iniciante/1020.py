# -*- coding: utf-8 -*-

ageInDays = int(input())

years = int(ageInDays / 365)
months = int((ageInDays % 365) / 30)
days = int(((ageInDays % 365) % 30))

print('%d ano(s)' % years)
print('%d mes(es)' % months)
print('%d dia(s)' % days)
