def is_even(number):

    if number % 2 == 0 :
        print('your number even')

    else:
        print('your number odd')

while True:
    number = int(input('введите число: '))
    print(is_even(number))

even_odd()

def say_hello():
    print('Hello world')

say_hello()


def create_list():
    my = []
    print(my)

create_list()

def calc():
    print(3+5)

calc()

def my1():
    x = ['pavel', 'jordan', 'pasha']
    if 'jordan' in x:
        print(x)
    else:
        pass  #пропустить

my1()

def create_list():
    my = []
    return my

print(create_list())

def create_instructors():
    instructor = {'name': 'jordan', 'age':21, 'job':'programmer'}

    if 'name' in instructor:
        return 'Да есть'
    else:
        return 'Не понимаб о чем вы'

print(create_instructors())

def spam(a,b,c=2):
    return a * b * c
print(spam(3,6))

def spam(a,b):
    return a + b
print(spam(3,6))


all_products = {'cklad': {'name':'хлеб', 'quantity':34 }}

def get_products(a = 'name'):
    print(all_products['cklad'][a])

get_products()

# *args - задавать любое кол-во аргументов

def spam1(*args):
    return sum(args)

print(spam1(1,2,3,4,4,5))

# *kwargs - задавать любое кол-во аргументов (ключ:значение)

def spam3(**kwargs):
    return kwargs

print(spam3(name='my', num=23))


