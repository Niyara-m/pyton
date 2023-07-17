class BankAccaunt:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def cash(self, amount):
        self.balance -= amount

    def my_balance(self):
        return self.balance

client_name = input('введите имя')
client1 = BankAccaunt(client_name)

while True:
    choice = int(input('1-deposit, 2-cash, 3-balance'))

    if choice == 1:
        how_much = int(input("Сумма депозита"))
        client1.deposit(how_much)

    elif choice == 2:
        how_much = int(input("Сумма ввывода"))
        client1.cash(how_much)

    elif choice == 3:
        print(client1.my_balance())

    else:
        print('I dont understand you')



client.deposit(67)
print(client.balance)

# class Comment:
#     def __init__(self, username, text, likes='normal'):
#         self.username = username
#         self.text = text
#         self.likes = likes
#
# user = Comment('Nikita', 'I want travel to Baku', 'cool')
# user2 = Comment('Nikita', 'I want travel to Baku')
# print(user.likes)
# print(user2.likes)
#
# методы локальны фун-ии глобальны

# class User:
#     name = 'jordan'
#
# class Person:
#     name = 'Jordan'
#     age = 23
#     job = 'programmer'
#
# class Game:
#     pass
#
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#     def stop(self):
#         print('Car is stoping')
#
#     def change_color(self,new_color):
#         self.color = new_color
#
# gentra = Car('Chevrolet', 'black', 2021)
# print(gentra.color)
#
# #смеена цвета машины у объекта
# gentra.change_color('white')
# print(gentra.color)
#
# print(gentra.year)
