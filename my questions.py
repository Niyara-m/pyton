names = ['Ivan', 'Pavel', 'Jordab', 5]
for i in range(1,20):
    if 'Pavel' in names:
        print('Pasha in the list')
    else:
        print('List is empty')
# ---------question 1 ------------
# Вопрос: Иван, Павел,Жордан не в диапвзоне 1-20. Только 5 там .
# значмт 1 раз повториться должно. Если range - это кол-во повторенией.
# Почему просто его не указать. Зачем пробегаться по массиву

# ---------question 2 ------------
p = ['m', 'my', 23]
i = 0
while i < len(p):
    print(p[i])
    i = i + 1
# Вопрос: Пока индекс < длины массива - выводить элемент списка. Зачем писать индекс = индекс + 1


# ---------question 3 ------------
mylist = [i for i in range(1,11,2)]
print(mylist)

#Просто видимо плохо поняла range)

# ---------question 4 ------------
# prazdniki = {'navruz' : '21march', 'New year' : '31december'}
# day = input('What date?')
#
# print(prazdniki.get(day))
#Задача от 6 урока. Не поняла ее работу


# ---------question 5 ------------
b = lambda y, u:y+u
print(b(2,3))
#Задача от 7 урока. Не поняла ее работу. Почему 5. я же 2 аргумента передала, и параметров 2

# ---------question 6 ------------
# import requests
# url = 'http://example.com/post'
# data = {'name':'john', 'age':30}
# response = requests.post(url, data=data)
# print(response.text)
#Задача от 8 урока. Что делает этот код

# ---------question 7 ------------
class MyClass:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_string(cls, string):
        return cls(int(string))

my_obj = MyClass.from_string('10')
print(my_obj.value)

#Задача от 10 урока. Что делает этот код я поняла, а вот объяснение кода не совсем

# ---------question 8 ------------
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rectangle = Rectangle(4,5)
print(rectangle.area)

#Задача от 10 урока. Что делает этот код я поняла, а вот объяснение кода не совсем