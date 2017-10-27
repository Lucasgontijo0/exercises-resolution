# -*- coding utf-8 _*-

notas = map(float, input().split(" "))
notas = list(notas)
media = (notas[0] * 2 + notas[1] * 3 + notas[2] * 4 + notas[3]) / 10

print('Media: %.1f' % media)

if media >= 7.0:
    print('Aluno aprovado.')
elif media >= 5.0 and media < 7.0:
    print('Aluno em exame.')
    exam_value = float(input())
    print('Nota do exame: %.1f' % exam_value)
    new_media = (media + exam_value) / 2.0
    if new_media >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' % new_media)
else:
    print('Aluno reprovado.')
