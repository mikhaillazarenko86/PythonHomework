# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и 
# возводит число А в целую неотрицательную степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
def degree(a, b):
    prod = 1
    if b == 0:
        return prod
    else:
        prod = prod * a
        b -= 1
        print(b, prod)
        return degree
print(degree(int(input('Введите число a:')),int(input('Введите степень b:'))))
    