all_products = {'Весь склад':{'яблоко': 4,'персик': 3}}
korzina = {'яблоко': 1,'персик': 2}

for v in all_products.values():
    admin = input('Что вы хотите сделать? ')
    if admin.lower() == 'заменить':
        whats_change = input('Введите название продукта: ')
        if whats_change in korzina.keys():
            change_product = input('Введите название продукта: ')
            quantity = int(input('сколько? '))
            korzina.pop(whats_change)
            korzina[change_product] = quantity
            print(f'Товар в корзине успешно изменен {korzina}')
        else:
            print('Такого Продукта нет в корзине')
    elif admin.lower() == 'удалить':
        whats_delete = input('Введите название продукта для удаления: ')
        if whats_delete in korzina.keys():
            korzina.pop(whats_delete)
            print(f'Товар в корзине успешно удален {korzina}')
        else:
            print('Такого Продукта нет в корзине')

    else:
        print('не понимаю о чем вы')