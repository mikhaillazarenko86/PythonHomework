def find():
    with open('tel.txt','r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Введите значение для поиска: ')
        for i in book:
            if temp in i:
                print(f'{book.index(i)}. {i}')
        