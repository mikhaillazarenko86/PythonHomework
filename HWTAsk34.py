# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает,
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает
# в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  
# def char(x):
#     return x % 2
# def same_by(characteristics, objects):
#     objects = list(map(characteristics, objects))
#     if len(objects) == 1:
#         return True
#     return 'Парам пам-пам' 
    
# mass = [1, 2, 4, 6]
# print(same_by(char,mass))
text = list(input('введите фразу: ').split())
def syllable(string):
    syllable_count = []
    for i in range(len(string)):
        count = 0
        for j in string[i]:
            if j in 'аеёиоуыэюя':
                count += 1
        syllable_count.append(count)
    return syllable_count
    
def rifma(syllable_count):
    count = 1
    for i in range(len(syllable_count) - 1):
        if syllable_count[i] == syllable_count[i + 1]:
            count += 1
        if count == len(syllable_count):
            a = 'Парам пам-пам'
        else:
            a = 'Пам парам'
    return a
print(rifma(syllable(text)))
   





    
