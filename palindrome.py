while True:
    word = input("Введите Ваше слово: ")

    reverse_word = list(word)
    reverse_word.reverse()
    reverse_word = ''.join(reverse_word)

    if word == reverse_word :
        print(f'Ваше слово "{reverse_word}" Палиндром!')
    else:
        print(f'Ваше слово "{word}" не палиндром!')
