# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.

# Ввод:
# 6
# Вывод
# 1 2 4
# Ввод
# 24
# Вывод
# 1 2 4 8 16
n = int(input('Введите число: '))
a = 2
k = -1
s = 0
while s < n:
    k += 1
    s = a ** k
    if s < n:
        print(s)
