# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11
import random

# num = input()
# sumnum = 0
# num2 = num.replace(',',"")
# for i in range(len(num2)):
#     sumnum += int(num2[i])
# print(sumnum)

# n = input()
# summa = 0
# for el in n:
#     if el != '.':
#         summa += int(el)
# print(summa)

# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input())
# x = 1
# d = []
# for i in range(1, n+1):
#     x *= i
#     d.append(x)
# print(d)

# Задайте список из n чисел последовательности (1 + 1 / n) ** n
# и выведите на экран их сумму.
#
# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#
# n = int(input())
# d = {n: round((1 + 1 / n) ** n, 3) for n in range(1, n + 1)}
# print(f' Список: {d}\n Сумма: {sum(d)}')

# n = int(input())
# d = []
# for x in range(1, n + 1):
#     d.append(round((1 + 1 / x) ** x, 3))
# print(d)
# print(sum(d))

# n = int(input())
# summa = 0
# for i in range(1, n + 1):
#     summa += (1 + 1 / i) ** i
# print(summa)

# Реализуйте алгоритм перемешивания списка.

# d = list(range(1, 20))
# print(d)
# random.shuffle(d)
# print(d)
