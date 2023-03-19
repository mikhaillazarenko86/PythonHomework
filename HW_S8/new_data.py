def add_data():
    fio = input('Введите ФИО: ')
    tel = input('Введите телефон: ')
    raz = ' | '
    info = fio + raz + tel
    with open('tel.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{info}')
