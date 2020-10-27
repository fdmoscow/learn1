# balance = 5 #создали переменну balance и присвоили значение -10
#price = 10
# print(bool(balance < 0 or price > balance)) #bool проверяет True или False и выводит эти значения () - обязательны
# or - это оператор или!

# if balance <0 or price > balance: #двоеточие и в теле оператора if пишем, что сделать
# в if скобки не обязательны
#   print('Пожалуйста, пополните баланс!')

#balance = 100
#price = 200

# if balance > price:
#   print('Спасибо за покупку')

# else: #иначе
#   print('Пожалуйста, пополните баланс')

#temperature = 17

# if temperature < 0:
#   print('На улице холодно!')
# elif 1 <= temperature <= 15: #elif - еще, также
#   print('На улице прохладно!')
# elif 16 <= temperature <= 25:
#   print('На улице тепло!')
# else:
#   print('На улице жарко!')

# реализуем в виде Функции
# def weather(temperature):
#   if temperature < 0:
#      return('It is cold outside')
# elif 1 <= temperature <= 15:
#    return ('It is chilly today')
# elif 16 <= temperature <= 25:
#    return ('It is a nice day today')
# else:
#   return ('Welcome to the decert')


# print(weather(-20))
# print(weather(100))
# print(weather(15))


#phone1 = {'name': 'IPhone Xs Plus', 'stock': 24,
 #         'price': 6453.73, 'discount': 15}
#phone2 = {'name': 'Samsung Galaxy S10',
 #         'stock': 8, 'price': 50000.00, 'discount':10}
#phone3 = {'name': 'HHH',
 #         'stock': 18, 'price': 1000.00, 'discount':10}
# добавили именованный параметр name!
#def discounted(price, discount, max_discount=20, name=''):
 #   price = abs(float(price))
  #  discount = abs(float(discount))
   # max_discount = abs(float(max_discount))
    #if max_discount > 99:
     #   raise ValueError('Слишком большая максимальная скидка')
    #if discount >= max_discount or "iphone" in name.lower() or not name:  # приводим данные в name к нижнему регистру
        # если iphone, то скидок нет, or not name - значит если name - пустая строка.
     #   return price
    #else:
     #   return price - (price * discount / 100)


#apple = discounted(phone1['price'], phone1['discount'], name=phone1['name'])  # передаем name я явном виде
#print(apple)

#android = discounted(phone2['price'], phone2['discount'], name=phone2['name'])
#print(android)

#noname = discounted(phone3['price'], phone3['discount'], name=phone3['name'])
#print(noname)


#age = int(input('Введите ваш возраст: '))

#def how_old (age):
 #   if 5 < age <= 7:
  #      return ('Детский сад')
   # elif 8 <= age <= 17:
    #    return ('Школьник')
    #elif 18 <= age <= 22:
     #   return ('Студент')
    #else:
     #   return ('Работает')

#time_machine = how_old(age)
#print(time_machine)



line1 = input('Напишите что нибудь: ')
line2 = input('Напишите что-нибудь: ')

def check (line1, line2):
    if type(line1) and type(line2) is not str:
        return(0)
    elif len(line1) == len(line2):
        return(1)
    elif len(line1) != len(line2) and len(line1) > len(line2):
        return(2)
    else:
        len(line1) != len(line2) and line2 == learn
        return(3)

test = check (line1, line2)
print(test)
        



