# -*- coding:utf-8 -*-

correct_password = 2002

password = 0
while password != correct_password:
    password = int(input())
    if password != correct_password:
        print("Senha Invalida")

print("Acesso Permitido")
