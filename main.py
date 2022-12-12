import random


def is_valid(string, upper):
    return 1 <= int(string) <= upper


def get_guess(upper):
    while True:
        guess = input(f'Введите число от 1 до {upper}: ')
        if is_valid(guess, upper):
            return int(guess)
        else:
            print(f'А может быть все-таки введем целое число от 1 до {upper}?')


def play():
    print('Добро пожаловать в числовую угадайку')
    upper = int(input("Введите верхнюю границу: "))
    target = random.randint(1, upper)
    counter = 0
    while True:
        answer = get_guess(upper)
        if answer < target:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1
        elif answer > target:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
        else:
            print('Вы угадали, поздравляем!')
            counter += 1
            break
    print(f'Вам понадобилось {counter} попыток.')
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    if input('Хотите сыграть снова? д/н: ') == 'д':
        play()


play()