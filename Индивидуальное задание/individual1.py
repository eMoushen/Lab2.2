#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Ввод номера месяца
    m = int(input('Введите номер месяца: '))

    # Проверка на число
    if m == 1:
        print('Январь')
    elif m == 2:
        print('Февраль')
    elif m == 3:
        print('Март')
    elif m == 4:
        print('Апрель')
    elif m == 5:
        print('Май')
    elif m == 6:
        print('Июнь')
    elif m == 7:
        print('Июль')
    elif m == 8:
        print('Август')
    elif m == 9:
        print('Сентябрь')
    elif m == 10:
        print('Октябрь')
    elif m == 11:
        print('Ноябрь')
    elif m == 12:
        print('Декабрь')
    else:
        print('Ошибка')