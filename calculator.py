class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(f'сложение: {self.a + self.b}')

    def multiplication(self):
        print(f'умножение: {self.a * self.b}')

    def division(self):
        print(f'деление: {self.a / self.b}')

    def subtraction(self):
        print(f'вычитание: {self.a - self.b}')


a = int(input("Введите A: "))
b = int(input("Введите B: "))

object = Math(a, b)

object.addition()
object.multiplication()
object.division()
object.subtraction()
