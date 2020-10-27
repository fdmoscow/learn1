#price = 100
#discount = 5
#price_with_discount = price - price * discount / 100
# print(price_with_discount) этот вариант не работает! нужна функция!

# def discounted(price, discount):
#price_with_discount = price - (price - discount / 100)
# print (price_with_discount)#функуция заканчивается где заканчивается отстут
# вызвать Ф можно по названию и передав туда данные
# discounted(100, 50) #100 - price, 50 - discount
# discounted(200, 30)#мы можем исползовать Ф для разных данных, не нужно постоянно переписывать
#discounted(500, 20)

# def discounted (price, discount):
# price = abs(float(price)) #еще добавим abs - модуль, убирает знак минус, float - вечественные числа
#discount = abs(float(discount))
# if discount >= 100: #если скидка больше или равна 100
#    price_with_discount = price # то мы просто возвращаем цену (нас хотят обмануть и скидку мы не считаем)
# else:
#    price_with_discount = price - (price * discount / 100)
# return (price_with_discount) #Ф возвращает результат своей работы

# p = discounted (100, 50) #результат мы кладем в переменную и выводим на экран (или использовать в расчетах)
# print(p)

# def discounted (price, discount):
#price = abs (float(price))
# discount = abs (float(discount)
# if discount >= 100:
#price_with_discount = price
# else:
#price_with_discount = price - (price * discount / 100)
# return price_with_discount

#product = {'name': 'Samsung Galaxy 10', 'stock': 8, 'price': 50000.0, 'discount': 50}

# product ['with_discount'] = discounted (product['price'], product['discount']) #добавляем новый элемент, приравниваем
# его к Ф и передаем в качестве переменных значение цены и скидки

# print(product)

# Позиционные аргументы
# discounted (100, 50, 5) #в Ф указаны 2 аргумента, а мы передаем 3 и 1 - ошибка
#discounted (100)

# def discounted (price, discount, max_discount = 70):  # добавляем именованный аргумент
#   price = abs(float(price))
#  discount = abs(float(discount))
# max_discount = abs(float(max_discount))
# if max_discount > 99:
#   raise ValueError ('Максимальная скидка не может быть больше 99%')# вызываем исключение

#    if discount >= max_discount: #здесь ограничение скидка не может былть больше или равной именованному агрументу
#       price_with_discount = price
#  else:
#      price_with_discount = price - (price * discount / 100)
# return price_with_discount


# product = {'name': 'Samsung Galaxy 10',
# 'stock': 10, 'price': 50000.0, 'discount':85, 'max_discount ': 80}

#product['with_discount'] = discounted(product['price'], product['discount'])

# print(product)
# print(discounted(100, 60)) #нужно print иначе Ф не выведет результат

def get_sum(one, two, delimeter='&'):
    one = str(one).capitalize()
    two = str(two).capitalize()
    print(one, delimeter, two)


get_sum(one='learn', two='python')


def format_price(price):
    price = int(price)
    return price
    print(f'Цена {price} рублей')

a = format_price(54.75)
print(a)


def greet(name):
    return(f'Hello {name} how are doing today?')
    
print(greet('Sasha'))
