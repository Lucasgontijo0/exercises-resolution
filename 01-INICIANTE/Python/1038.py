# -*- coding:utf-8 -*-

lunch  = {
    1:{ 'description':'Cachorro Quente', 'price':4.00 },
    2:{ 'description':'X-Salada', 'price':4.50 },
    3:{ 'description':'X-Bacon', 'price':5.00 },
    4:{ 'description':'Torrada Simples', 'price':2.00 },
    5:{ 'description':'Refrigerante', 'price':1.50 }
}

itens = map(int, input().split(" "))
item, quantity = itens
value = lunch[item]['price'] * quantity
print('Total: R$ %.2f' % value)
