import math


def division(first_num, second_num):
    if second_num != 0:
        print(first_num / second_num)
    if isinstance(first_num, float) or isinstance(second_num, float):
        return print(first_num / second_num)
    else:
        return print('Что-то пошло не так. Проверьте корректность введеных данных')


def multipl(first_num, second_num):
    if isinstance(first_num, int) or isinstance(second_num, int):
        return print(first_num * second_num)
    if isinstance(first_num, float) or isinstance(second_num, float):
        return print(first_num * second_num)
    else:
        print('Что-то пошло не так. Проверьте корректность введеных данных')


def addition(first_num, second_num):
    if isinstance(first_num, int) or isinstance(second_num, int):
        return print(first_num + second_num)
    if isinstance(first_num, float) or isinstance(second_num, float):
        return print(first_num + second_num)
    else:
        print('Что-то пошло не так. Проверьте корректность введеных данных')


def substraction(first_num, second_num):
    if isinstance(first_num, int) or isinstance(second_num, int):
        return print(first_num - second_num)
    if isinstance(first_num, float) or isinstance(second_num, float):
        return print(first_num - second_num)
    else:
        print('Что-то пошло не так. Проверьте корректность введеных данных')


def enlarging(first_num, second_num):
    if isinstance(first_num, int) or isinstance(second_num, int):
        return print(first_num ** second_num)
    if isinstance(first_num, float) or isinstance(second_num, float):
        return print(first_num ** second_num)
    else:
        print('Что-то пошло не так. Проверьте корректность введеных данных')


def sinus(first_num):
    if first_num > 0 and (isinstance(first_num, int) or isinstance(first_num, float)):
        return print(math.sin(math.radians(first_num)))
    else:
        print('Что-то пошло не так. Проверьте корректность введеных данных')


def cosinus(first_num):
    if isinstance(first_num, int) or isinstance(first_num, float):
        return print(math.cos(math.radians(first_num)))
    else:
        print('Что-то пошло не так. Проверьте корректность введеных данных')


def tangens(first_num):
    if first_num > 0 and (isinstance(first_num, int) or isinstance(first_num, float)):
        return print(math.tan(math.radians(first_num)))
    else:
        print('Что-то пошло не так. Проверьте корректность введеных данных')


def square_root(first_num):
    if isinstance(first_num, int) or isinstance(first_num, float):
        return print(math.sqrt(first_num))
    else:
        print('Что-то пoшло не так. Проверьте корректность введеных данных')


while True:
    print('Добро пожаловать в консольный инженерный калькулятор!')
    print('Выберете желаемое действие: ')
    print('*Примечание: Если у Вас действие с 6 по 9 включительно вводить второе число не требуется!')
    print('1. Деление')
    print('2. Умножение')
    print('3. Сумма')
    print('4. Разность')
    print('5. Возведение в степень')
    print('6. Косинус угла')
    print('7. Синус угла')
    print('8. Тангенс угла')
    print('9. Извлечение квадратного корня')
    print('10. Выход')

    choose = input('Введите номер операции (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):  ')

    if choose == '10':
        print('Выход из программы')
        break

    if choose in ('1', '2', '3', '4', '5'):
        first_number = float(input('Введите первое число: '))

    if choose in ('1', '2', '3', '4', '5'):
        second_number = float(input('Введите второе число: '))

    if choose in ('6', '7', '8', '9'):
        number_special = float(input('Введите одно число: '))

    elif choose == '1':
        print('Результат:', division(first_number, second_number))

    elif choose == '2':
        print('Результат:', multipl(first_number, second_number))

    elif choose == '3':
        print('Результат:', addition(first_number, second_number))

    elif choose == '4':
        print('Результат:', substraction(first_number, second_number))

    elif choose == '5':
        print('Результат:', enlarging(first_number, second_number))

    if choose == '6':
        print('Результат:', sinus(number_special))

    if choose == '7':
        print('Результат:', cosinus(number_special))

    if choose == '8':
        print('Результат:', tangens(number_special))

    if choose == '9':
        print('Результат:', square_root(number_special))

else:
    print('Некорректный ввод. Попробуйте ввести другое число.')
