my_contacts = ['Nika', 'Regina', 'Juliya']

# exapmple 1 перевернуть слова в списке
reverse_text = [item[::-1] for item in my_contacts]

print(reverse_text)

# exapmple 2 Все слова в списке в верхнем регистре
upper_list = [item.upper() for item in my_contacts]

print(upper_list)

# exapmple 3 Все слова в списке в нижнем регистре
lower_list = [item.lower() for item in my_contacts]

print(lower_list)

# exapmple 4 Первые буквы слов в списке
first_word = [item[0].upper() for item in my_contacts]

print(first_word)

# exapmple 5 Отобразить числа меньше 5 в диапазоне от 1 до 10
newlist = [x for x in range(10) if x < 5]

print(newlist)


# exapmple 6 Отобразить слова в прошедшем времени
words = ['adopt', 'bake', 'beam', 'confide', 'grill', 'wave' ]
past_tense = [i + 'ed' if i[-1] != 'e' else i +'d' for i in words]

print(past_tense)

# exapmple 7 Отобразить слова с буквой А в слове
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)