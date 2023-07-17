my_contacts = ['nika', 'regina', 'juliya']
action = input('Какое действие со списком контактов вы хотите совершить: Удалить, Изменить, Добавить? ')

if action == 'Добавить' :
    contact = input('Введите Имя для добавления: ')
    if contact in my_contacts:
        print('Такой контакт уже есть')
    else:
        my_contacts.append(contact)
        print(my_contacts)

elif action == 'Удалить' :
    contact = input('Введите Имя для удаления: ')
    if contact in my_contacts:
        my_contacts.remove(contact)
        print(my_contacts)
    else:
        print('Вы ввели контакт которого нет в списке')

elif action == 'Изменить' :
    element = int(input('Введите порядковый номер контакта который хотите заменить: '))
    if element <= len(my_contacts) - 1 :
        contact = input('Введите имя контакта: ')
        my_contacts[element] = contact
        print(my_contacts)
    else:
        print('в списке меньше элементов')
else:
    print('Не понятно что вы ввели')