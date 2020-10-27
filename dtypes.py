a = 2  # integer
b = 3
c = a + b
print(c)

a1 = 2  # division float
b1 = 2
c1 = a1 / b1
print(c1)

a = 3  # bool
b = 0
c = a != b
print(c)

a = 'Hello'  # string
b = 'hello'
c = a == b
print(c)

a = 'Привет'  # add strings
b = 'Мир'
c = a + ' ' + b + '!'  # not the best way
print(c)  # не получается складывать строки с целыми или вещ числами

a = 'Привет'  # format
b = 'Мир'
c = 3
# кавычки-усики это шаблок, потом format и переменные
c = '{} {}{}!'.format(a, b, c)
print(c)  # можно складывать разные типы данных

user = 'Python'  # именованный аргумент
# name - символ подстановки кавычки-усики
c = 'Привет {name}!'.format(name=user)
print(c)

user = 'Миша'  # f строки лучшее форматирование
b = f'Привет {user}!'  # такая переменная должна существовать
print(b)

a = 'Привет'
b = 'Мир!'
c = f'{a} {b}'
print(len(c))  # len - длинна строки

a = 'Привет'.upper()
print(a)

a = 'Hello'.lower()
print(a)

a = 'hello'.capitalize()
print(a)

# Убрать пробелы
a = '   Миша  '
b = a.strip()  # пробелы убираются
print(len(b))  # 4 символа
print(len(a))  # 9 символов

# replace замена символов
a = 'Прив3т т3б3'
b = a.replace('3', 'e')
print(a)  # без замены
print(b)  # c заменой

a = 'Тебе приветЫ'
b = a.replace('Ы', '')
print(b)  # произошла замена
print(a)  # без замены

a = 'ПриветЫ мир'
b = a.replace('мир', 'PYTHON') .replace('Ы', '')  # 2 замены
print(b)  # вывод на печать с заменой
print(a)

# Split разбиение
a = 'learn.python.ru'
print(a.split('.'))  # разбиваем строку в список по точке (.)

a = 'Предложение из нескольких слов 127'
b = a.split()  # ничего в скобках тогда split будет разбивать по всем знакам (пробел, два пробела итд)
print(b)
print(len(b))  # 5 - кол-во слов в предложении

# None (отсутствует значение исользуется is или is not)
a = None
b = 0
print(a is None)  # True
print(b is None)  # False
print(b is not None)  # True

# типы переменных type
a = 2.0
b = 3
c = '5'
d = True
e = None
print(type(a))  # float
print(type(b))  # int
print(type(c))  # string  смотрим какие типы переменных
print(type(d))  # bool
print(type(e))  # NoneType

# Ввод от пользователя
# name = input('Введите имя пользователя: ') #name - переменная, = - присвоить, input () - строка для пользователя как запрос
# print(f'Привет {name}!') #выводим на экран строку f' и подставляем значение переменной name

#age = input ('Сколько Вам лет? ')
# age = 2019 - age #нельзя вычитать строку из числа!!!
#print('Ваш возраст {age}')
# поэтому нужно привести к строку к типу integer
#age = int(input('Введите Ваш возраст: '))
#age = 2019 - age
#print(f'Вы родились в {age} году')

print(bool('Hello'))
print(bool(0))
print(bool(-1))
print(bool(None))
print(bool())

a = 2.0
b = str(a)
print(type(b))

#ДЗ
#v = int(input('Введите число от 1 до 10: '))
#print(v)
#print(v+10)

#name = input('Введите Ваше имя: ')
#print(f'Привет {name}! Как дела?')

print(float(-1))


