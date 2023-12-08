import math


def Division(first_num, second_num):
    if second_num != 0:
        print(first_num / second_num)
    if isinstance(first_num, float) or isinstance(second_num, float):
        return print(first_num / second_num)
    else:
        return print('Что-то пошло не так. Проверьте корректность введеных данных')


def Multipl(first_num, second_num):
    if isinstance(first_num, int) or isinstance(second_num, int):
        return print(first_num * second_num)
    if isinstance(first_num, float) or isinstance(second_num, float):
        return print(first_num * second_num)
    else:
        print('Что-то пошло не так. Проверьте корректность введеных данных')


def Addition(first_num, second_num):
    if isinstance(first_num, int) or isinstance(second_num, int):
        return print(first_num + second_num)
    if isinstance(first_num, float) or isinstance(second_num, float):
        return print(first_num + second_num)
    else:
        print('Что-то пошло не так. Проверьте корректность введеных данных')


def Substraction(first_num, second_num):
    if isinstance(first_num, int) or isinstance(second_num, int):
        return print(first_num - second_num)
    if isinstance(first_num, float) or isinstance(second_num, float):
        return print(first_num - second_num)
    else:
        print('Что-то пошло не так. Проверьте корректность введеных данных')


def Enlarging(first_num, second_num):
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


def Square_Root(first_num):
    if isinstance(first_num, int) or isinstance(first_num, float):
        return print(math.sqrt(first_num))
    else:
        print('Что-то пошло не так. Проверьте корректность введеных данных')
