# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые 
# должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
def show_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
    return book

def new_data():
    fio = input('Введите ФИО: ')
    tel = input('Введите телефон: ')
    raz = ' | '
    info = fio + raz + tel
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write(f'\n{info}')
    

def find_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        temp = input('Введите значение для поиска: ')
        for i in file:
            if temp in i:
                print(i)
    return i

def del_data():
    with open('data.txt', 'w', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Введите значение для удаления: ')
        for i in book:
            if temp in i:
                print(f'Удалить {i} ?')
                book.pop(book.index(i))
        print(book)

  
    
while True:
    mode = input('выберите режим работы справочника(1 - просмотр, 2 - добавление записи, 3 - поиск записи, 4 - удаление записи, 0 - выход): ')
    if mode == '1':
        print(show_data())
    elif mode == '2':
        new_data()
    elif mode == '3':
        find_data()
    elif mode == '4':
        del_data()
    elif mode == '0':
        break
    else:
        print('No mode')