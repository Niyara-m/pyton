# цикл while
names = ['ivan', 'pavel', 'jordan']

while True:
    new = input('Кого добавим? ')
    names.append(new)
    print(names)


# цикл while
p = ['m', 'my', 23]
i = 0

while i < len(p):
    print(p[i])
    i += 1

# цикл for
names = ['jordan', 'ivan', 'pavel', 5]

for i in range(1, 4) :
    if 'pavel' in names :
        print('pavel есть в списке')
    else:
        print('Не понимаю о ком вы')


# неправильные глаголы

words = ['adopt', 'bake', 'beam', 'confide', 'grill', 'wave' ]
past_tense = []

for i in words :
    if i[-1] != 'e' :
        past_tense.append(i + 'ed')
    else :
        past_tense.append(i +'d')

print(past_tense)





nums1 = [i for i in range(1,21)]
nums2 = [i for i in nums1 if i % 2 == 0]
print(nums2)



names = ['Pavel', 'Sasha', 'Jordan', 'Pasha']
answer = [i[0] for i in names ]
print(answer)


my_list = [i for i in range(1, 11, 2)]
print(my_list)

names = ['pavel', 'jordan', 'sasha']
names2 = [name for name in names if 'o' in name ]


print(names2)








names = ['nika', 'kolya', 'sergey']
names1 = [i.upper() for i in names]

print(names1)

text = 'nika'
reverse_text = text[::-1]
print(reverse_text)

usernames = []
while True:
    names = input('Введите имя: ')

    if names in usernames:
        print('Такой юзер имеется попробуйте другой')
    else:
        usernames.append(names)
        print('Username успешно добавлен')
        print(usernames)


