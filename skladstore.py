all_products = {'Весь склад':{}}

for v in all_products.values():
    admin = input('Что вы хотите сделать? ')
    if admin.lower() == 'добавить':
        product_name = input('Введите название продукта: ')
        product_count = int(input('Введите кол-во: '))

        all_products['Весь склад'][product_name] = product_count
        print(all_products)

    elif admin.lower() == 'продукты':
        print(all_products)

    else:
        print('не понимаю о чем вы')