user1 = input('введите Ваше имя: ')
user1choiсe = input('выберите камень ножницы или бумага: ')

user2 = input('введите Ваше имя: ')
user2choiсe = input('выберите камень ножницы или бумага: ')

if user1choiсe == user2choiсe :
    print('Ничья')
elif user1choiсe == 'камень' and user2choiсe == 'ножницы' :
    print(f'{user1} выиграл')
elif user1choiсe == 'камень' and user2choiсe == 'бумага' :
    print(f'{user2} выиграл')
elif user1choiсe == 'ножницы' and user2choiсe == 'камень' :
    print(f'{user2} выиграл')
elif user1choiсe == 'ножницы' and user2choiсe == 'бумага' :
    print(f'{user1} выиграл')
elif user1choiсe == 'бумага' and user2choiсe == 'камень' :
    print(f'{user1} выиграл')
elif user1choiсe == 'бумага' and user2choiсe == 'ножницы' :
    print(f'{user2} выиграл')
else:
    print('Вы ввели неправильное значение')
