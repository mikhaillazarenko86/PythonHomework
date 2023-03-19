from new_data import add_data
from show_data import show
from find_data import find
while True:
    mode = input('выберите режим работы справочника(1 - просмотр, 2 - добавление записи, 3 - поиск записи, 4 - удаление записи, 0 - выход): ')
    if mode == '1':
        show()
    elif mode == '2':
        add_data()
    elif mode == '3':
        find()
    elif mode == '4':
        del_data()
    elif mode == '0':
        break
    else:
          print('No mode')
