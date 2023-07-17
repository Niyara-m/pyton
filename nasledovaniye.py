class Animal:
    def make_sound(self,s):
        print(s)

class Horse(Animal):
    pass

mustang = Horse()

mustang.make_sound('igogo')

# ----Множественное наследование----
# class Car:
#     def __init__(self,model,color,year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# class SuperCar(Car):
#     def __init__(self,model,color,year,sponsor):
#         super().__init__(model,color,year)
#         self.sponsor = sponsor
#
# gentra = Car('Chevrolet', 'Black', 2022)
# amgone = SuperCar('Mersedes', 'Silver', 2023, 'Petrones')
#
# print(amgone.sponsor)

#
# ----PARENTS----
# class Parent:
#     def swearing(self):
#         print('Ругается')
#
#     def loving(self):
#         print('Любить')
#
# class Child(Parent):
#     def study(self):
#         print('учиться')

# ------Множественное наследолвание ------
# class Animal:
#     def make_sound(self,s):
#         print(s)
#
# class Horse:
#     def dibi(self):
#         print('Встала на дыбы')
#
# class Pony(Animal, Horse):
#     pass
#
# pony1 = Pony()
# pony1 = dibi()
# pony1 = Pony()

#------ @classmethod--------
# class Animal:
#     @classmethod
#     def make_sound(cls,s):
#         print(s)
#
# Animal.make_sound('fffff')


# class Myclass:
#     def __init__(self, value):
#         self.value = value
#
#     @classmethod
#     def from_string(cls, string):
#         #берем строку переводим в числовое зн-е
#         return cls(int(string))
#
# my_obj = Myclass.from_string('10')
# print(my_obj.value)


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.width * self.height
#
# rectangle = Rectangle(4,5)
# print(rectangle.area)
#
# rectangle.width = 6
# print(rectangle.area)


# class Worker:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     def register_new_worker(self):
#         print('Работает')

# class BigWorker(Worker):
#     def __init__(self, name, position):
#         super().__init__(name, position)
#
#     def show_info(self, name):
#         return name.position
#
# jordan = Worker('Artem', 'junior')
# pavel = BigWorker('Pavel', 'HR')
#
# jordan.register_new_worker()
# print(pavel.show_info(jordan))

class Player:
    def __init__(self, speed, power, accuracy, stamina):
        self.speed = speed
        self.power = power
        self.accuracy = accuracy
        self.stamina = stamina

class Atacker(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super().__init__(speed, power, accuracy, stamina)

    def goal(self):
        print('Забил гол')


class Goalkeeper(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super().__init__(speed, power, accuracy, stamina)

    def keep_goal(self):
        print('Удержал мяч и не дал забить гол')


class Defender(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super().__init__(speed, power, accuracy, stamina)

    def keep_goal(self):
        print('Удержал мяч и не дал забить гол')


    #test git


