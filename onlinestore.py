all_products = {'Весь склад':{'яблоко': 4,'персик': 3}}
korzina = {}

for v in all_products.values():
    admin = input('Что вы хотите сделать? ')
    if admin.lower() == 'добавить':
        product_name = input('Введите название продукта: ')
        product_count = int(input('Введите кол-во: '))

        if product_name in all_products['Весь склад'].keys():
            all_products['Весь склад'][product_name] = all_products['Весь склад'][product_name] + product_count
            print( all_products)
        else:
            all_products['Весь склад'][product_name] = product_count
            print(all_products)

    elif admin.lower() == 'купить':
        whats_buy = input('Введите название продукта: ')
        if whats_buy in all_products['Весь склад'].keys():
            how_much = int(input('сколько? '))
            all_products['Весь склад'][whats_buy] = all_products['Весь склад'][whats_buy] - how_much
            korzina[whats_buy] = how_much

            print(f'Продукт добавлен в корзину!!! Ваша корзина: {korzina}')
            print(f'Продукт успешно списан со склада {all_products}')
        else:
            print('Продукта нет на складе')

    elif admin.lower() == 'заменить':
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

    elif admin.lower() == 'продукты':
            print(all_products)

    else:
        print('не понимаю о чем вы')