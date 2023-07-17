import random
guess = random.randint(1,50)

mynumber = int(input('Какое число загадал компьюьер? '))

if mynumber == guess:
    print(f'Вы угадали число! Компьютер загадал {guess}')

else:
    print(f'Вы НЕ угадали число! Компьютер загадал {guess}')