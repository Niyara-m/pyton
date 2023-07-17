clients = {}
opened_rooms = [i for i in range(1, 21)]
busy_rooms = []

def add_client(name, room):
        clients[name] = room
def del_client(name):
        clients.pop(name)
def show_busy_rooms():
        return busy_rooms

client_name = input('Добро пожаловать! Введите свое имя! ')
while True:
        admin = int(input('1 - Регистрация, 2 - Удалиться из базы, 3 - Увидеть занятые номера'))

        if admin == 1:
                print(opened_rooms)
                client_room = int(input('Какой номер хотите занять? '))
                opened_rooms.remove(client_room)
                busy_rooms.append(client_room)
                add_client(client_name, client_room)
                print('Вы зарегистрировались!')
        elif admin == 2:
                opened_rooms.append(clients[client_name])
                busy_rooms.remove(clients[client_name])
                del_client(client_name)
                print('Приходите ещё!')
        elif admin == 3:
                print(show_busy_rooms())