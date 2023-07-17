#Тема словарей

x = {'name':'pasha', 'job':'tg company'}

print(x['name'], x['job'])

#вывод jordan s
data = {'name' : ['Jordan', 'Pavel'],
        'age': (12,21),
        'job': 'programmers'}

print(data['name'][0], data['job'][-1])


#вывод методов словарей
instructors = {'name':'jordan', 'age':21, 'job':'programmer'}
print(instructors.values())
print(instructors.keys())
print(instructors.items())


# добавление ключа и значения
instructors['hobby'] = 'reading'

print(instructors)


# добавление ключа и значения в словарь
Caffes = {'evos': {'gorod': 'tashkent', 'fillial': 'many', 'open year': 2007}}
Caffes['evos']['kitchen']= 'fast food'
Caffes['KFC'] = {'gorod': 'fergana', 'filiallov': 'many', 'opened': 2019}

print(Caffes)

# Удаление в словарях
my_dict = {'song': 'godzila', 'singer': 'eminem', 'genre': 'hip-hop'}
print(my_dict)

#цикл словорей
instructor = dict(name='jordan', age=23, job='pyton')
for v in instructor.values():
    print(v)

for k, v in instructor.items():
    print(k,v)

# проверка ключа
if 'jordan' in instructors.values():
    print('Yes')
else:
    print("Don't have")


#вывод jordan s
x = input('Введите имя:')
y = {'name': x,
     'course': 'pyton developer'}
print(y['name'])



