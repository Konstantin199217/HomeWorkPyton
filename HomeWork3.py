# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# num_list = list(map(int, input().split()))
# num_list2 = []
# i = 0
# while i < len(num_list):
#     if i % 2 == 1:
#         num_list2.append(num_list[i])
#     i += 1
# print(num_list)
# print(num_list2)
# print(sum(num_list2))

# range(1, len(some), 2)#  range с ходом через один

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# my_lyst = list(map(int, input().split(', ')))
# size = len(my_lyst)
# if len(my_lyst) % 2 != 0:
#     size = len(my_lyst) // 2 + 1
# else:
#     size = len(my_lyst) // 2
# new_list = []
# for i in range(size):
#     new_list.append(my_lyst[i] * my_lyst[len(my_lyst) - i - 1])
# print(new_list)

# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# num_list = list(map(float, input().split(', ')))
# num_list2 = []
# for i in num_list:
#     if i%1 != 0:   # Так ответ нужный, но у 5 значение будет 0 и значит оно же минимальное а не 0.1??? Или я не правильно понял
#         num_list2.append(round(i % 1, 2))
# print(f'{num_list} \n{num_list2} \n Максимальное: {max(num_list2)} \n Минимальное: {min(num_list2)}')
# print(f' Разность: {max(num_list2) - min(num_list2)}')


# some_list=[input() for _ in range(int(input()))]
# minn = 1
# maxx = 0
# for el in some_list:
#     if '.' in el:
#         if float('0.' + el.split('.')[1]):
#             maxx = float('0.' + el.split('.')[1])
# print(maxx - minn)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input())
# print(bin(num))
# lin = ''
# while num > 0:
#     lin = str(num % 2) + lin
#     num = num // 2
# print(lin)

#
# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# k = int(input())
# some_list = [0] * (2 * k - 1)
# some_list[k + 1] = 1
# for i in range(k + 2, 2 * k + 1):
#      some_list[i] = some_list[i - 1] + some_list[i - 2]
# for i in range(k - 1, -1, -1):
#     some_list[i] = some_list[i + 2] - some_list[i + 1]
# print(some_list)