# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
#
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
#
# print('Введите цифру, обозначающую день недели (от 1 до 7) и я скажу вам выходной это или нет:')
# num = int(input())
# if num == 6 or num == 7:
#     print('Да')
# else:
#     print('Нет')

# day = int(input())
# day_name = {1: 'Понедельник',
# 2: 'Вторник',
# 3: 'Среда',
# 4: 'Четверг',
# 5: 'Пятница',
# 6: 'Суббота',
# 7: 'Воскресенье'}
# print(day_name.get(day, 'Такого дня недели не существует'))

# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in (True, False):
#     for y in (True, False):
#         for z in (True, False):
#             some_str = (not(x or y or z) == (not x and not y and not z))
#             print(f'x = {x} y = {y} z = {z} -> {some_str}')
#
# for i in range(0b111 + 1):
# binary_string = format(i, '03b')
# x = int(binary_string[0])
# y = int(binary_string[1])
# z = int(binary_string[2])
# print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} есть {not (x or y or z) == (not x) and (not y) and (not z)}')

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
#
# print('Введите ваши координаты через запятую:')
# some_str = input().split(', ')
# x = int(some_str[0])
# y = int(some_str[1])
# if x > 0 and y > 0:
#     print('1')
# if x < 0 and y > 0:
#     print('2')
# if x < 0 and y < 0:
#     print('3')
# if x > 0 and y < 0:
#     print('4')

# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# print('Введите четверть и узнаем диапазон возможных координат:')
# num = int(input())
# if num ==1:
#     print('x   y')
#     for i in range(0, 6):
#         for j in range(0, 6):
#             print(i, + j, sep=', ')
# if num ==2:
#     print('x   y')
#     for i in range(0, 6):
#         for j in range(0, 6):
#             print(i*-1, + j, sep=', ')
# if num ==3:
#     print('x   y')
#     for i in range(0, 6):
#         for j in range(0, 6):
#             print(i*-1, + j*-1, sep=', ')
# if num ==4:
#     print('x   y')
#     for i in range(0, 6):
#         for j in range(0, 6):
#             print(i, + j*-1, sep=', ')

# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# print('Введите координаты двух точек:')
# x1, y1 = map(int, input().split(','))
# x2, y2 = map(int, input().split(','))
# print(round(((x2-x1)**2+(y2-y1)**2)**0.5, 3))

# import math
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# ac = y2 - y1
# bc = x2 - x1
# print(round((ac ** 2 + bc ** 2) ** 0.5, 2))
# print(int(math.sqrt(ac ** 2 + bc ** 2) * 100) / 100)
# print(str(math.sqrt(ac ** 2 + bc ** 2)).split('.')[0] + '.' + str(math.sqrt(ac ** 2 + bc ** 2)).split('.')[1][:2])