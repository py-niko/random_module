while True:
    from random import*
    print('Добро пожаловать в угадай число! Мы ради тебя видеть! Напиши максимальное число для загадывания числа от 1 до Лимита!')
    limit = input('Лимит: ')

    def is_valid(n):
        if n.isdigit() == True and limit.isdigit() == True and 1 <= int(n) <= int(limit):
            return True
        else:
            return False


    #основная игра
    def game():
        num = randint(1,int(limit))
        counter = 0
        while True:
            n = input('Введите число: ')
            if is_valid(n) == False:
                print('Вы вели некорретное число для нашей игры')
            else:
                n = int(n)
                if n == num:
                    counter += 1
                    print(f'Поздравляю вы выиграли Ваша попытка {counter}')
                    break
                elif n > num:
                    counter += 1
                    print('Выше число больше загаданного')
                elif n < num:
                    counter += 1
                    print('Выше число меньше загаданного')


        print(f'Спасибо за игру! Еще раз ("ДА", "НЕТ")?')
        answer = input()
        N = ['нет', 'no', 'н', 'y', 'ytn']
        Y = ['да','д', 'а', 'l', 'lf']
        if answer.lower() in N:
            print('Еще увидимся! \nПока! \n\n\n\n\n')

        elif answer.lower() in Y:
            while True:
                game()
        else:
            print('Я вас не понимаю! Играем или нет?')


    game()


