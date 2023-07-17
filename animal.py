class Animal:
    def make_sound(self,s):
        print(s)

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Cow(Animal):
    pass

xaski = Dog()
Persian = Cat()
Ayrshire_cow = Cow()

xaski.make_sound('Gav')
Persian.make_sound('Myau')
Ayrshire_cow.make_sound('Mu')