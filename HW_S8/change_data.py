with open('data.txt','r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Введите значение для поиска: ')
        for i in book:
            if temp in i:
                print(f'{book.index(i)}. {i}')
temp = int(input('Введите номер записи: '))
if temp == book.index(i):
    # book.pop(book.index(i))
    # print(book)
    # print(' '.join(map(str, book)))
    fio = input('Введите ФИО: ')
    tel = input('Введите телефон: ')
    raz = ' | '
    info = fio + raz + tel
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(info)
    
