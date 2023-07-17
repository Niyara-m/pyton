classroom = {'Katya': 5, 'Igor': 2, 'petya':7}

def add_people():
    name = input('Введите имя ученика: ')
    student_class = input('Введите класс ученика: ')
    classroom[name] = student_class
    print(classroom)

def delete_people():
    name_delete = input('Введите имя ученика для удаления: ')
    if name_delete in classroom.keys():
        classroom.pop(name_delete)
        print(f'ученик успешно удален {classroom}')
    else:
        print('Такого ученика нет')

def change_people():
    name_change = input('Введите имя: ')
    if name_change in classroom.keys():
        name_for_change = input('Введите имя: ')
        classroom_count = int(input('Введите класс? '))
        classroom.pop(name_change)
        classroom[name_for_change] = classroom_count
        print(f'Ученик успешно изменен {classroom}')
    else:
        print('Такого ученика нет')

for people in classroom:
    while True:
        admin = input('Что вы хотите сделать? Добавить Удалить или Изменить ученика ')
        if admin.lower() == 'добавить':
            add_people()

        elif admin.lower() == 'удалить':
            delete_people()

        elif admin.lower() == 'изменить':
            change_people()
        else:
            print('не понимаю о чем вы')