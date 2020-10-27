list = [3, 5, 7, 9, 10.5]
print(list)

list.append('Python')

print(list)

print(len(list))

print(list[0])

print(list[-1])

print(list[2:5])

del list[5]
print(list)

# СЛОВАРИ

product = {
    'name': 'Iphone Xs',
    'stock': 24,
    'price': 6574.9
}

print(product)
print(len(product))

product['stock'] = 10
product['price'] = 45055
product['memory'] = 64  # можно добавить новые данные в словарь

print(product)

# получаем (выводим) значение элемента по названию пример
# пишем в скобках название словаря и в квадрытных скобках название элемента
print(product['name'])
print(product['stock'])
print(product['memory'])
print(product['price'])
# print(product['discount'])#ошибка тк нет такого элемента в словаре
print(product.get('name'))  # альтернативный способ вызова элемента
print(product.get('discount'))  # показывает не ошибку а none

# С помощью .get можно задать значение, если ключа НЕТ в словаре

# выводится значение 0 по умолчанию (например скидка)
print(product.get('discount', 0))

# значение не была, выведил, что подскавили
print(product.get('country', 'US'))

# удаление del pruduct и ключ, который хотим удалить
del product['stock']
print(product)


# Объединение словарей и списков
phones = ["Samsung Galaxy S10", "iPhone Xs", "XiaoMi"]

product = {
    'name': 'Iphone Xs',
    'stock': 24,
    'price': 6574.9
}

print(product)

# здесь добавляем значение (ключ) recomend и присваеваем ему значение списка phones
product['recomend'] = phones

print(product)

phones = ["Samsung Galaxy S10", "iPhone Xs", "XiaoMi"]

product = {
    'name': 'Iphone Xs',
    'stock': 24,
    'price': 6574.9,
    'recomend': phones,
}

print(product['recomend'])
print(product['recomend'][1])  # выводится 1 элемент списка recomend

product['recomend'].append('IPHONE6')  # добавляем элемент в список
print(product['recomend'])

# Список словарей
stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1,
     'recomended': ['Samsung Galaxy S10', 'iPhone Xs']},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5}
]

print(stock)
print(stock[0])  # выводим первый словарь {}
print(stock[0]['name'])  # выводим из 1го словаря значение name

print(stock[0])
# положили в значение stock 0 price - 10000, простой способ увеличить
stock[0]['price'] += 10000
print(stock[0])



# Homework
gorod = {
    "city": "Москва", 
    "temperature": "20"
    }

print(gorod['city'])

gorod['temperature'] = '15'
print(gorod)

print(gorod.get('country'))

print(gorod.get('country', 'Russia'))

gorod['data'] = "27.05.2019" #добавляем элемент, скобки квадратные

print(gorod)
print(len(gorod))
