# Вычислить число c заданной точностью d
#
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
#
# d = str(input('Задайте точночть: '))
# c = len(d) - 2
# p = math.pi
# print(d)
# print(c)
# print(round(p, c))


# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
#
# num = int(input())
# simple = []
# d = 2
# while num > 1:
#     if num % d == 0:
#         simple.append(d)
#         num = num/d
#     else:
#         d += 1
# print(simple)

# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

#
# a = [int(i) for i in input('Задайте последовательнось чисел через пробел: ').split()]
# unik = []
# for i in a:
#    if a.count(i) == 1:
#        unik.append(i)
# print(unik)




# Не судите строго))

# Задана натуральная степень k.
# Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import sympy
from sympy import solve
import random

# a = int(input('Введите степнь: '))
# x = sympy.Symbol('x')
# l = [random.randint(0, 100) for _ in range(5)]
# f = int(random.randint(1, 4))
# y = 0
# if f == 1:
#     y = l[0] * x ** a
# if f == 2:
#     y = l[0] * x ** a + l[1] * x
# if f == 3:
#     y = l[0] * x ** a + l[1] * x - l[3]
# with open('File.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{y}' + '= 0' + '\n')


# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
a = 2
x = sympy.Symbol('x')
l = [random.randint(0, 100) for _ in range(7)]
f = int(random.randint(1, 4))
g = 0
if f == 1:
    g = l[0] * x ** a
if f == 2:
    g = l[0] * x ** a + l[1] * x
if f == 3:
    g = l[0] * x ** a + l[1] * x - l[2]
with open('File1.txt', 'w', encoding='utf-8') as file:
    file.write(f'{g}' + '\n')
r = int(random.randint(1, 4))
z = 0
if r == 1:
    z = l[3] * x ** a
if r == 2:
    z = l[3] * x ** a + l[4] * x
if r == 3:
    z = l[3] * x ** a + l[4] * x - l[5]
with open('File2.txt', 'w', encoding='utf-8') as file:
    file.write(f'{z}' + '\n')

with open('File1.txt', 'r', encoding='utf-8') as file:
    file.seek(0, 0)
    y = file.read().splitlines()

with open('File2.txt', 'r', encoding='utf-8') as file:
    file.seek(0, 0)
    y2 = file.read().splitlines()

print(y, y2)
ot = sympy.solve(y + y2)
with open('File.txt', 'w', encoding='utf-8') as file:
    file.seek(0, 0)
    file.write(f'{ot}')
print(ot)