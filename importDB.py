

def import_txt():
    path_to_file = 'phonebook.txt'
    return print(path_to_file)


def import_csv():
    import csv
    path_to_file = 'phonebook.csv'
    results = []
    with open (path_to_file) as csvfile:                           
        # Создаем объект reader, указываем символ-разделитель ";"
        file_reader = csv.reader(csvfile, delimiter= ";")
        for row in file_reader:
            results.append(row) # Каждую строку из телефонной книги добавляем в список результатов
    return results

def import_json():
    path_to_file = 'phonebook.json'
    return print(path_to_file)

# Выбираем формат файла телефонной книги
def choice_format():
    print('Телефонную книгу в каком формате будете импотировать? \n.txt - 1 .csv - 2 .json - 3:')
    choice = int((input()))
    match choice:
        case 1: return import_txt()
        case 2: return import_csv()
        case 3: return import_json()
        case _ :
            print('Неизвестный формат файла')
            exit()

choice_format()
print(import_csv())   

