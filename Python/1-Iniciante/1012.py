# -*- coding utf-8 -*-

line = map(float, input().split(" "))
A, B, C = line

baseTriangulo = A * C / 2
areaCirculo = 3.14159 * (C ** 2)
areaTrapezio = C * (A + B) / 2
areaQuadrado = B * B
areaRetangulo = A * B

print('TRIANGULO: %.3f' % baseTriangulo)
print('CIRCULO: %.3f' % areaCirculo)
print('TRAPEZIO: %.3f' % areaTrapezio)
print('QUADRADO: %.3f' % areaQuadrado)
print('RETANGULO: %.3f' % areaRetangulo)
