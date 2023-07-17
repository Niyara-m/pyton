#exercise 8
souvenir = 75
bauble = 112

quantity_souvenir = int(input('Введите количество сувениров: '))
quantity_bauble = int(input('Введите количество безделушек: '))

amaunt = souvenir * quantity_souvenir + quantity_bauble * bauble
amaunt_kg = amaunt / 1000

print(f'Общий вес посылки {amaunt} грамм, или {amaunt_kg} килограмм')



# exercise 7
number = int(input('Введите число: '))

if number > 0 :
    amaunt = (number * (number + 1)) / 2
    print(f'Сумма натуральных чисел  от 1 до {number} равна {"%.0f" % amaunt}')

else : print("Вы ввели отрицательное число")



#exercise 6
order_price = int(input('Введите сумму заказа: '))
tips = order_price * 18 / 100
tax = order_price * 12 / 100

print(f'Чаевые: {"%.2f" % tips}, налог: {"%.2f" % tax}, сумма чаевых и налога: {"%.2f" % (tips + tax)}')



#exercise 5
liter = 0.10
big_bottle = 0.25

quantity_bottle = int(input('Введите количество бутылок размером 1 литр: '))
quantity_big_bottle = int(input('Введите количество бутылок большого размера: '))

amaunt = quantity_bottle * liter + quantity_big_bottle * big_bottle

print(f'Сумма равна {"%.2f" % amaunt}')

