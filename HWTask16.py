# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве из случайных чисел. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint
k = int(input('Введите количество элементов в массиве:'))
list = [randint(1, 10) for i in range(k)]
n = int(input('Введите число для поиска:'))
count = 0
for i in range(k):
    if n == list[i]:
        count += 1
print(list)
print(count)
