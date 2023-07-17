class Car:
    def __init__(self, color, type,  year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')

    def stop(self):
        print('Автомобиль заглушен')

    def change_year(self,new_year):
        self.year = new_year
        print(gentra.year)

    def change_type(self, new_type):
        self.type = new_type
        print(gentra.type)

    def change_color(self, new_color):
        self.color = new_color
        print(gentra.color)

gentra = Car('black','Chevrolet', 2021)

gentra.start()
gentra.stop()
gentra.change_year(1940)
gentra.change_type('mercedes')
gentra.change_color('blue')