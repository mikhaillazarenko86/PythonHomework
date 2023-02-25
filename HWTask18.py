# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) 
# самый близкий по величине элемент к заданному числу X. Пользователь в 
# первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint
k = int(input('Введите количество элементов в массиве:'))
list = [randint(1, 10) for i in range(k)]
print(list)
list2 = []
n = int(input('Введите число для поиска:'))
for i in range(k):
    list2.append(abs(n - list[i]))
print(list2)
min = list2[0]
for i in range(len(list2)):
    if min > list2[i]:
        min = list2[i]
print(f"Ближайшее число к {n} равно {min + n}")    
