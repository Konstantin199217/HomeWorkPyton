# Задача
# 5.
# Дан список интов, повторяющихся элементов в списке
# нет.Нужно преобразовать это множество в строку,
# сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"
import math

# some_list = [1,4,5,2,3,9,8,11,0]
# some_list.sort()
# print((some_list))
# def chang(list):
#     some_str = []
#     mini = list[0]
#     count = list[0]
#     for i in range(len(list)):
#         if list[i] - count == 0:
#             count += 1
#             if list[i] == max(list):
#                 some_str.append(str(f'{mini} - {list[i]}'))
#                 break
#         else:
#             some_str.append(str(f'{mini}-{count - 1}'))
#             mini = list[i]
#             count = list[i] + 1
#         if list[i] == max(list):
#                 some_str.append(str(f'{list[i]}'))
#     return ','.join(some_str)
# print(chang(some_list))

# Планеты и орбиты
#S = p*a*b
#Пример:
#orbits = [(1,3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#print(*find_farthest_orbit(orbits))
# 2.5, 10
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# def find_farthest_orbit(orbits):
#     s = [3.14*max(x) for x in orbits]
#     return(orbits[s.index(max(s))])
#
# print(*find_farthest_orbit(orbits))