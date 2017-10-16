# -*- coding: utf-8 -*-

valorSegundos = int(input())

hours = int(valorSegundos / 3600)
minutes = int((valorSegundos % 3600) / 60)
seconds = int((valorSegundos % 3600) % 60)

print('%d:%d:%d' % (hours, minutes, seconds))
