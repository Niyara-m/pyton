users = {}
users['name'] = 'Niyara'
print(users)


caffees = {'evos': {'gorod':'tashkent','filialov':'monogo','otk':2007}}

caffees['evos']['kuxnya'] = 'fast food'
print(caffees)


def even_odd():
    while True:
        number = int(input('введите число '))

        if number%2 == 0:
            print('your number is четное')
        else:
            print('your number is нечетное')

even_odd()