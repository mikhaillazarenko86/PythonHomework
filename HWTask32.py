# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
data = list(map(int, input('Введите число: ').split()))
min = int(input("Введите нижний предел: "))
max = int(input("Введите верхний предел: "))
print(data)
 for i in range(len(data)):
     if data[i] > min and data[i] < max:
         print(f'Индекс числa {data[i]} в диапазоне от {min} до {max} равен {i}')
# res = list(filter(lambda x: x > min and x < max, data))
# print(res)