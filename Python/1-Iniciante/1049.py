# -*- coding:utf-8 -*-

subfilo = input()
classe = input()
habito_alimentar = input()

animais = {
    'vertebrado':{
        'ave':{
            'carnivoro':'aguia',
            'onivoro':'pomba'
        },
        'mamifero':{
            'onivoro':'homem',
            'herbivoro':'vaca'
        }
    },
    'invertebrado':{
        'inseto':{
            'hematofago':'pulga',
            'herbivoro':'lagarta'
        },
        'anelideo':{
            'hematofago':'sanguessuga',
            'onivoro':'minhoca'
        }
    }
}

print(animais[subfilo][classe][habito_alimentar])