test = 'kirov'
print(test[::-1])


name = ['mirik', 'javlon','kamich','tima']

admin = input('что хотите сделать? ')
if admin == "добавить":
    new_name = input('введи новое имя: ')
    name.append(new_name)
    print(name)
elif admin == "удалить":
    delete_name = input('Введи кого хочешь удалить: ')
    name.remove(delete_name)
    print(name)
elif admin == "заменить":
    staroe_name = input('введите кого хотите заменить: ')
    staroe_name_index = name.index(staroe_name)
    staroe_name = input('введите на кого хочешь заменить: ')
    name[staroe_name_index] = staroe_name
    print(name)
else:
    print('введи верно пацан')