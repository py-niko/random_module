from random import*

#Входные данные
num = str(randint(1,100))
k = [str(i) for i in range(1,101)]
print('Добро пожаловать в числовую угадайку')

# Функция корректности данных
def is_valid(s):
    if s in k:
        return True
    else:
        return False

#Функция сравнения
def comparison(s):
    if num == s:
        print('Вы угадали, поздравляем!', 'Спасибо, что играли в числовую угадайку. Еще увидимся...', sep = '\n')
        return print(f'Количество попыток: {count}')
    elif num > s:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print('Ваше число больше загаданного, попробуйте еще разок')
count = 0
# цикл игры
while True:
    s = input('Введите число от 1 до 100: ')
    count += 1
    if is_valid(s) == True:
        comparison(s)

    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
    count = 0
    print(num)


