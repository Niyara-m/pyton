names = []
numbers = []
services = []

while True:
    item = input('Что хотите ввести: имя, номер, услуга? ')
    if item == 'имя' :
        name = input('введите Ваше имя? ')
        names.append(name)
        print(names)

    elif item == 'номер' :
        number = input('введите Ваш номер? ')
        numbers.append(number)
        print(numbers)

    elif item == 'услуга' :
        service = input('введите Вашу услугу? ')
        services.append(service)
        print(services)
    else:
        print('Вы ввели не правильную инфу')
